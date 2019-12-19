from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from traffic_permit import views
"""
-路由系统：
    路由创建参数
        第一个位置参数：
            路由path
        第二个参数：
            注册的视图集
        第三个参数：
            DRF会根据执行的动作类型，拼接此参数，形成url_name，用于反向reverse，此处并没有使用到
            
        Tips:
            SimpleRouter在注册路由的时候，已经为路径补全了末尾斜杠，所以下面就不用再写斜杠
            在url的调用中，除了get请求，django会补齐，并且301跳转，其余方法都不会有此行为
            所以好的习惯是在每个url请求调用中，末尾都加上斜杠
"""
router = SimpleRouter()
router.register(r'traffic_permit', viewset=views.TrafficPermitView, base_name='traffic_permit')
router.register(r'unit', viewset=views.UnitView, base_name='unit')
router.register(r'tp_transit_time', viewset=views.TrafficPermitCategoryTransitTimeView, base_name='tp_transit_time')
urlpatterns = [
]

urlpatterns += router.urls
