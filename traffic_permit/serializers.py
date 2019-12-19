from rest_framework import serializers
from traffic_permit.models import TrafficPermit, \
    Unit, TrafficPermitCategoryTransitTimeRel
"""
-DRF序列化器为程序完成了数据的序列化和反序列化操作：
    序列化：
        将数据库数据经过逻辑处理，序列化成JSON，返回给前端
    反序列化：
        接收前端上传的数据，验证其有效性，存储db
        
-序列化器创建及属性
    创建：
        只需继承serializers.ModelSerializer
    属性：
        model ：
            声明序列化器操作的数据模型
        fields：
            要序列化展示的字段，可以为'__all__',全部字段，也可以是一个元组或者列表类型
        depth:
            外键到其他模型的model可以通过此参数，控制展示深度，默认0，只展示外键模型的id值
            
-序列化器嵌套
    model及序列化器的主从关系：
        首先这里规定，主动声明关系的表为从表，如此demo的traffic_permit,
        被动被声明关系的表为主表，如此demo的unit
    创建嵌套关系：
        主表的序列化器可以声明从表的序列化器，字段名称为从表声明ForeignKey时的related_name参数值，
        形成序列化器的嵌套，实现在展示主表时候，附带从表信息
"""


class TrafficPermitSerializer(serializers.ModelSerializer):
    # #显示可读类型 v1 以SerializerMethodField形式实现
    # vehicle_plate_color = serializers.SerializerMethodField()
    # vehicle_category = serializers.SerializerMethodField()
    # category = serializers.SerializerMethodField()
    # validity_category = serializers.SerializerMethodField()
    # register_channel = serializers.SerializerMethodField()
    # #显示可读信息 如 车辆类型，车牌颜色 ，通行证类型
    # @staticmethod
    # def get_vehicle_plate_color(instance):
    #     return instance.get_vehicle_plate_color_display()
    #
    # @staticmethod
    # def get_vehicle_category(instance):
    #     return instance.get_vehicle_category_display()
    #
    # @staticmethod
    # def get_category(instance):
    #     return instance.get_category_display()
    #
    # @staticmethod
    # def get_validity_category(instance):
    #     return instance.get_validity_category_display()
    #
    # @staticmethod
    # def get_register_channel(instance):
    #     return instance.get_register_channel_display()

    class Meta:
        model = TrafficPermit
        # 除了db存储的原生字段，额外返回一些字段的可读类型，新增这些字段，只会作为只读返回，即post写操作无需声明新增的可读字段
        fields = [instance.name for instance in TrafficPermit._meta.fields] + \
                 [
                     'get_vehicle_plate_color_display',
                     'get_vehicle_category_display',
                     'get_traffic_permit_category_display',
                     'get_validity_category_display',
                     'get_register_channel_display',
                     'get_traffic_permit_status_display'
                 ]
        depth = 1  # 控制反向关联时的展示深度


class UnitSerializer(serializers.ModelSerializer):
    traffic_permits = TrafficPermitSerializer(many=True, read_only=True)

    class Meta:
        model = Unit
        fields = [instance.name for instance in Unit._meta.fields] + ['traffic_permits'] + [
            'get_unit_category_display',
            'get_unit_status_display',
        ]


class TrafficPermitCategoryTransitTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrafficPermitCategoryTransitTimeRel
        fields = [instance.name for instance in TrafficPermitCategoryTransitTimeRel._meta.fields] + [
            'get_traffic_permit_category_display',
            'get_transit_start_time_display',
            'get_transit_end_time_display',
        ]
