from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from traffic_permit.models import TrafficPermit, Unit, TrafficPermitCategoryTransitTimeRel
from traffic_permit.serializers import TrafficPermitSerializer, UnitSerializer, \
    TrafficPermitCategoryTransitTimeSerializer

"""
-DRF ModelViewSet：
    简介：此类继承了很多的Mixin类，封装了很全面的方法，来对应HTTP基础动作。
-视图的创建：
    创建视图类，继承ModelViewSet, 便包含了所有基础HTTP方法
    在类中必须声明两个属性：
        queryset 返回和接收的实例对象集合
        serializer_class 要使用的序列化器
-自定义方法@action的创建
    简要说明：
        除了封装的基础HTTP方法，DRF还支持自定义方法，来满足业务上的不同需求
    创建：
        定义一个函数，用此装饰器装饰@action
        此装饰器有两个参数
            @action(methods=[], detail=True/False)
            methods:
                声明允许访问的http方法
            detail:
                声明是否在url路径中取pk值
-视图的调用（url形态）
    在下的urls.py中注册路由
    路由前缀就包含了所有的http基础方法，以此demo中的unit数据集合为例：
        1.在url中注册路由
            router.register(r'unit', viewset=views.UnitView, base_name='unit') 其中UnitView就是views中编写的视图类
        2.该url表现形态为：
            http://ip:port/apps/unit/ 其中apps为root下的url中的根路由，unit为router注册路由
        3.基础HTTP方法调用说明
            GET http://ip:port/apps/unit/
                获取所有的unit信息
            GET http://ip:port/apps/unit/1/
                获取id为1的单位信息
            POST http://ip:port/apps/unit/
                新增一个单位
            PUT http://ip:port/apps/unit/1/
                完整修改一个单位
            PATCH http://ip:port/apps/unit/1/
                部分修改一个单位
            DELETE http://ip:port/apps/unit/1/
                删除一个单位
        4.自定义方法调用说明
            以此方法为例：
                @action(methods=["get"], detail=False)
                def my_func(self, request):
                    pass
            调用方法，detail=False 时:
                GET http://ip:port/apps/unit/my_func/ 
                    使用自定义方法规定允许的请求方式，函数名my_func被当做了url路径
            调用方法，detail=True 时:
                GET http://ip:port/apps/unit/1/my_func/
                    使用自定义方法规定允许的请求方式，函数名my_func被当做了url路径，pk值在unit和my_func之间
                    此时获取pk值的方式
                    @action(methods=["get"], detail=True)
                def my_func(self, request, pk):
                    instance = Instance.objects.get(id=pk)
                    pass
"""


class BaseView(ModelViewSet):
    """
    TODO: 复写更多父类方法，以适应业务场景
    """

    # 复写父类方法，将物理删除改为逻辑删除
    def perform_destroy(self, instance):
        instance.active = False
        instance.save()


class TrafficPermitView(BaseView):
    queryset = TrafficPermit.objects.filter(active=True)
    serializer_class = TrafficPermitSerializer

    # 复写父类create 根据业务逻辑，对资源新增做一定的限制
    def create(self, request, *args, **kwargs):
        # TODO：复写父类create，对instance根据业务逻辑，进行判断，此方法也可以写为@action自定义方法，由前端选择调用时机

        # 该复写方法实现新增通行证时，自动检测通行证类别和通行证允许通行时间关联表，不符合规则则不能新增
        request_data = self.request.data

        # 获取通行证类型
        tp_category = request_data.get('traffic_permit_category', '')

        # 获得通行证类型准许通行时间 实例
        allow_transit_instance = TrafficPermitCategoryTransitTimeRel.objects.get(traffic_permit_category=tp_category)

        if allow_transit_instance:
            # 上传实例选择的通行时间
            transit_start_time = request_data.get('transit_start_time', '')
            transit_end_time = request_data.get('transit_end_time', '')

            # 准许通行时间表的准许通行时间
            allow_transit_start_time = allow_transit_instance.transit_start_time
            allow_transit_end_time = allow_transit_instance.transit_end_time

            # 做逻辑对比
            if transit_start_time < allow_transit_start_time or transit_end_time > allow_transit_end_time:
                return Response(
                    data={'error': '请在正确的时间段内选择通行时间{}-{}'
                          .format(allow_transit_instance.get_transit_start_time_display(),
                                  allow_transit_instance.get_transit_end_time_display())},
                    status=status.HTTP_400_BAD_REQUEST)

        # 父类原来的逻辑：获得序列化器，验证合法性，创建实例，返回response
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UnitView(BaseView):
    queryset = Unit.objects.filter(active=True)
    serializer_class = UnitSerializer

    # 此方法操作修改unit的standard状态，将单位置为 标杆单位/非标杆单位
    @action(methods=['put'], detail=False)
    def change_unit_standard(self, request):
        state = request.data.get('state')
        unit_names = request.data.get('unit_names')

        if not (state or unit_names):
            return Response(data={'error': '请传入state和unit_names参数'}, status=status.HTTP_400_BAD_REQUEST)

        units = Unit.objects.filter(unit_name__in=unit_names)

        if not units:
            return Response(data={'error': '未找到指定单位'}, status=status.HTTP_404_NOT_FOUND)

        standard = None
        if state == 'to_standard':
            standard = True
        elif state == 'not_standard':
            standard = False
        else:
            return Response(data={'error': '请传入规定内的state参数：to_standard/not_standard'},
                            status=status.HTTP_400_BAD_REQUEST)

        units.update(standard=standard)

        return Response(data={'success': '单位[{}]已经全部置为{}'.format(
            str([unit.unit_name for unit in units]), '标杆单位' if standard else '非标杆单位'
        )})

    # 此函数为UnitView下的一个自定义动作，返回所有的标杆单位
    @action(methods=['get'], detail=False)
    def get_standard_units(self, request):

        units = Unit.objects.filter(active=True, standard=True)

        if not units:
            return Response(status=status.HTTP_404_NOT_FOUND)

        ser = UnitSerializer(instance=units, many=True)

        return Response(data=ser.data, status=status.HTTP_200_OK)

    # 此函数将标杆单位下的所有车辆置为正常状态
    @action(methods=['put'], detail=False)
    def unfreeze_traffic_permit(self, request):
        units = Unit.objects.filter(active=True, standard=True)

        if not units:
            return Response(status=status.HTTP_404_NOT_FOUND)

        for unit in units:
            if not unit.traffic_permits:
                continue
            unit.traffic_permits.update(traffic_permit_status=1)

        return Response(status=status.HTTP_200_OK)


class TrafficPermitCategoryTransitTimeView(BaseView):
    queryset = TrafficPermitCategoryTransitTimeRel.objects.filter(active=True)
    serializer_class = TrafficPermitCategoryTransitTimeSerializer


