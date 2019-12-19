from django.db import models
from new_weixin_pass.constant_mapping import VEHICLE_PLATE_COLOR, VEHICLE_CATEGORY, TRAFFIC_PERMIT_CATEGORY, \
    TRAFFIC_PERMIT_VALIDITY, TRAFFIC_PERMIT_ROUTE_CHANGE_TIMES, TRAFFIC_PERMIT_REGISTER_CHANNEL, UNIT_CATEGORY, \
    TRAFFIC_PERMIT_TRANSIT_TIME, TRAFFIC_PERMIT_STATUS, UNIT_STATUS

"""
-关于状态、类型等字段的存储：
    统一到项目root目录下的constant_mapping.py中获取，
    一律存储数字类型，还有一些布尔类型的字段，一律存为bool型，
    拒绝使用类似'01', '02'这种形态来标识状态、类型、有效性等等。
    实现存储的统一，展示的统一，避免歧义
    
-关于通用字段的解释：
    通用字段全部为缺省字段，都有其对应的默认值
    created_time datetime类型，数据被创建的时间点
    updated_time datetime类型，数据最后被修改的时间点
    active bool类型，数据有效性，是否被软删除
    memo textfield类型，数据的备注信息
"""


class TrafficPermit(models.Model):
    # foreign key
    unit = models.ForeignKey('Unit', related_name='traffic_permits', blank=True, null=True, default=None,
                             on_delete=models.SET_DEFAULT, verbose_name='所属单位')

    # driver
    driver_name = models.CharField(max_length=50, verbose_name='驾驶人')
    driver_license_number = models.CharField(max_length=100, verbose_name='驾驶证号')
    driver_phone = models.CharField(max_length=100, verbose_name='驾驶人手机号')

    # vehicle
    vehicle_number = models.CharField(max_length=100, verbose_name='车牌号码')
    vehicle_plate_color = models.IntegerField(choices=VEHICLE_PLATE_COLOR, verbose_name='车牌颜色')
    vehicle_category = models.IntegerField(choices=VEHICLE_CATEGORY, verbose_name='车辆类型')
    vehicle_mass = models.IntegerField(verbose_name='车辆质量')

    # traffic permit
    traffic_permit_category = models.IntegerField(choices=TRAFFIC_PERMIT_CATEGORY, verbose_name='通行证类别')
    start_point = models.CharField(max_length=50, blank=True, null=True, verbose_name='通行证起点')  # 通过put可以修改
    end_point = models.CharField(max_length=50, blank=True, null=True, verbose_name='通行证终点')
    via_point = models.TextField(blank=True, null=True, verbose_name='通行证途经点')
    transit_start_time = models.IntegerField(choices=TRAFFIC_PERMIT_TRANSIT_TIME, verbose_name='通行证规定开始通行时间')
    transit_end_time = models.IntegerField(choices=TRAFFIC_PERMIT_TRANSIT_TIME, verbose_name='通行证规定截止通行时间')
    validity_category = models.IntegerField(choices=TRAFFIC_PERMIT_VALIDITY, verbose_name='通行证有效期类型')
    effective_time = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='通行证生效时间')
    route_change_times = models.IntegerField(choices=TRAFFIC_PERMIT_ROUTE_CHANGE_TIMES,
                                             blank=True, default=3, verbose_name='通行证剩余线路修改次数')
    register_channel = models.IntegerField(choices=TRAFFIC_PERMIT_REGISTER_CHANNEL, verbose_name='通行证注册渠道')
    traffic_permit_status = models.IntegerField(choices=TRAFFIC_PERMIT_STATUS, blank=True, default=1)

    # universal
    created_time = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='数据创建时间')
    updated_time = models.DateTimeField(auto_now=True, blank=True, verbose_name='数据更新时间')
    active = models.BooleanField(blank=True, default=True, verbose_name='数据有效性')
    memo = models.TextField(blank=True, null=True, verbose_name='数据备注信息')

    class Meta:
        verbose_name = '通行证信息表'
        verbose_name_plural = verbose_name


class Unit(models.Model):

    # unit
    unit_name = models.CharField(max_length=100, verbose_name='单位名称')
    unit_category = models.IntegerField(choices=UNIT_CATEGORY, verbose_name='单位类别')
    unit_status = models.IntegerField(choices=UNIT_STATUS, blank=True, default=1)
    unit_address = models.TextField(verbose_name='单位地址')
    unit_principal = models.CharField(max_length=100, verbose_name='单位负责人')
    unit_phone = models.CharField(max_length=100, verbose_name='单位电话')
    standard = models.BooleanField(blank=True, default=False, verbose_name='是否为标杆单位')

    # universal
    created_time = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='数据创建时间')
    updated_time = models.DateTimeField(auto_now=True, blank=True, verbose_name='数据更新时间')
    active = models.BooleanField(blank=True, default=True, verbose_name='数据有效性')
    memo = models.TextField(blank=True, null=True, verbose_name='数据备注信息')

    class Meta:
        verbose_name = '单位信息表'
        verbose_name_plural = verbose_name


class TrafficPermitCategoryTransitTimeRel(models.Model):

    # traffic_permit
    traffic_permit_category = models.IntegerField(choices=TRAFFIC_PERMIT_CATEGORY, unique=True, verbose_name='通行证类型')
    transit_start_time = models.IntegerField(choices=TRAFFIC_PERMIT_TRANSIT_TIME, verbose_name='开始通行时间')
    transit_end_time = models.IntegerField(choices=TRAFFIC_PERMIT_TRANSIT_TIME, verbose_name='截止通行时间')

    # universal
    created_time = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='数据创建时间')
    updated_time = models.DateTimeField(auto_now=True, blank=True, verbose_name='数据更新时间')
    active = models.BooleanField(blank=True, default=True, verbose_name='数据有效性')
    memo = models.TextField(blank=True, null=True, verbose_name='数据备注信息')

    class Meta:
        verbose_name = '通行证种类允许通行时间关联表'
        verbose_name_plural = verbose_name


