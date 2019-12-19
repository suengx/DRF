
# Vehicle Category
SMALL_CAR = 1
BIG_CAR = 2
SMALL_TRUCKS = 3
BIG_TRUCKS = 4

VEHICLE_CATEGORY = (
        (SMALL_CAR, '小型客车'),
        (BIG_CAR, '大型客车'),
        (SMALL_TRUCKS, '小型货车'),
        (BIG_TRUCKS, '大型货车'),
    )

# Vehicle plate color
PLATE_COLOR_YELLOW = 1
PLATE_COLOR_BLUE = 2
PLATE_COLOR_GREEN = 3

VEHICLE_PLATE_COLOR = (
    (PLATE_COLOR_YELLOW, '黄牌'),
    (PLATE_COLOR_BLUE, '蓝牌'),
    (PLATE_COLOR_GREEN, '绿牌')
)


# Unit Status
UNIT_NORMAL = 1
LOST_TRUST_FREEZE = 2
UNIT_STATUS = (
    (UNIT_NORMAL, '正常'),
    (LOST_TRUST_FREEZE, '失信冻结')

)
# Unit Category
STATE = 1
PRIVATE = 2

UNIT_CATEGORY = (
    (STATE, '国营单位'),
    (PRIVATE, '私营单位'),
)

# TrafficPermit Status
TRAFFIC_PERMIT_NORMAL = 1
EMERGENCY_FREEZE = 2
HEAVY_POLLUTION_FREEZE = 3
HEAVY_GAS_FREEZE = 4
TRAFFIC_PERMIT_FREEZE_BY_UNIT = 5

TRAFFIC_PERMIT_STATUS = (
    (TRAFFIC_PERMIT_NORMAL, '正常'),
    (EMERGENCY_FREEZE, '紧急情况冻结'),
    (HEAVY_POLLUTION_FREEZE, '天气重污染冻结'),
    (HEAVY_GAS_FREEZE, '排放超标冻结'),
    (TRAFFIC_PERMIT_FREEZE_BY_UNIT, '企业关联冻结')
)
# TrafficPermit Category
DANGEROUS = 1
SEAFOOD = 2
MUCK = 3

TRAFFIC_PERMIT_CATEGORY = (
    (DANGEROUS, '危险品运输'),
    (SEAFOOD, '海产品运输'),
    (MUCK, '渣土运输'),
)

# TrafficPermit Transit Time
TRAFFIC_PERMIT_TRANSIT_TIME = (
    (0, '00:00:00'),
    (1, '01:00:00'),
    (2, '02:00:00'),
    (3, '03:00:00'),
    (4, '04:00:00'),
    (5, '05:00:00'),
    (6, '06:00:00'),
    (7, '07:00:00'),
    (8, '08:00:00'),
    (9, '09:00:00'),
    (10, '10:00:00'),
    (11, '11:00:00'),
    (12, '12:00:00'),
    (13, '13:00:00'),
    (14, '14:00:00'),
    (15, '15:00:00'),
    (16, '16:00:00'),
    (17, '17:00:00'),
    (18, '18:00:00'),
    (19, '19:00:00'),
    (20, '20:00:00'),
    (21, '21:00:00'),
    (22, '22:00:00'),
    (23, '23:00:00'),
)
# TrafficPermit Validity
ONE_DAY = 1
THREE_DAY = 2
ONE_MONTH = 3

TRAFFIC_PERMIT_VALIDITY = (
    (ONE_DAY, '一天'),
    (THREE_DAY, '三天'),
    (ONE_MONTH, '一个月'),
)

# Traffic Permit Route Change Times
ONCE = 1
TWICE = 2
THRICE = 3

TRAFFIC_PERMIT_ROUTE_CHANGE_TIMES = (
    (ONCE, '一次'),
    (TWICE, '两次'),
    (THRICE, '三次'),
)

# Traffic Permit Register Channel
Wechat = 1
PC = 2

TRAFFIC_PERMIT_REGISTER_CHANNEL = (
    (Wechat, '微信端'),
    (PC, 'PC端'),
)
# Illegal Category
EMISSION_EXCEED = 1
DASH_FORBIDDEN = 2

ILLEGAL_CATEGORY = (
    (EMISSION_EXCEED, '不安规定时间行驶'),
    (DASH_FORBIDDEN, '闯禁行')
)
