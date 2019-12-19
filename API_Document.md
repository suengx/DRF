[TOC]

#### Unit

##### 新增一个unit单位

- url: http://127.0.0.1:8000/apps/unit/

- 请求方法POST

- 请求参数

  ```python
  {
  	"unit_name": "文峰集团",
  	"unit_category": 2,  # int类型
  	"unit_address": "天府大街",
  	"unit_principal": "李主任",
  	"unit_phone": "13788662253"
  }
  ```

- 返回参数

  ```python
  {
      "id": 3,
      "unit_name": "文峰集团",
      "unit_category": 2,
      "unit_status": 1,
      "unit_address": "天府大街",
      "unit_principal": "李主任",
      "unit_phone": "13788662253",
      "standard": false,  # 缺省 默认false
      "created_time": "2019-12-18T08:27:16.586107Z",  # 缺省
      "updated_time": "2019-12-18T08:27:16.586149Z",  # 缺省
      "active": true,  # 缺省
      "memo": null,  # 缺省
      "traffic_permits": [],  # 缺省 若该单位下有通行证 会以列表形式返回
      "get_unit_category_display": "私营单位",  # 返回字段可读类型
      "get_unit_status_display": "正常"  # 返回字段可读类型
  }
  ```

##### 获得一个单位

- url: http://127.0.0.1:8000/apps/unit/3/

- 请求方法GET

- 无请求参数，注意url中pk值 这个例子为3，标识获得id为3的单位

- 返回参数

  ```python
  {
      "id": 3,
      "unit_name": "文峰集团",
      "unit_category": 2,
      "unit_status": 1,
      "unit_address": "天府大街",
      "unit_principal": "李主任",
      "unit_phone": "13788662253",
      "standard": false,
      "created_time": "2019-12-18T08:27:16.586107Z",
      "updated_time": "2019-12-18T08:27:16.586149Z",
      "active": true,
      "memo": null,
      "traffic_permits": [],
      "get_unit_category_display": "私营单位",
      "get_unit_status_display": "正常"
  }
  ```

##### 整体修改一个单位

- url: http://127.0.0.1:8000/apps/unit/3/

- 请求方法PUT

- 请求参数和POST一致，但性质视为完整修改一个已存在的资源

- 返回参数

  ```python
  {
      "id": 3,
      "unit_name": "文峰集团",
      "unit_category": 2,
      "unit_status": 1,
      "unit_address": "天府大街",
      "unit_principal": "李主任",
      "unit_phone": "13788662253",
      "standard": false,
      "created_time": "2019-12-18T08:27:16.586107Z",
      "updated_time": "2019-12-18T08:27:16.586149Z",
      "active": true,
      "memo": null,
      "traffic_permits": [],
      "get_unit_category_display": "私营单位",
      "get_unit_status_display": "正常"
  }
  ```

##### 部分修改一个单位

- url: http://127.0.0.1:8000/apps/unit/3/

- 请求方法PATCH

- 请求值为以下任意字段组合，不存在于该实例的字段值 会被忽略

  ```python
  {
      "unit_name": "文峰集团",
      "unit_category": 2,
      "unit_status": 1,
      "unit_address": "天府大街",
      "unit_principal": "李主任",
      "unit_phone": "13788662253",
      "standard": false,
      "created_time": "2019-12-18T08:27:16.586107Z",
      "updated_time": "2019-12-18T08:27:16.586149Z",
      "active": true,
      "memo": null,
  }
  ```

- 返回值

  ```python
  {
      "id": 3,
      "unit_name": "文文集团",
      "unit_category": 2,
      "unit_status": 1,
      "unit_address": "天府大街",
      "unit_principal": "李主任",
      "unit_phone": "13788662253",
      "standard": false,
      "created_time": "2019-12-18T08:27:16.586107Z",
      "updated_time": "2019-12-18T08:41:07.712669Z",
      "active": true,
      "memo": null,
      "traffic_permits": [],
      "get_unit_category_display": "私营单位",
      "get_unit_status_display": "正常"
  }
  ```

##### 删除一个单位

- url: http://127.0.0.1:8000/apps/unit/3/
- 请求方法DELETE
- 无请求参数，注意url路径中的pk值，这个例子中是3，标识删除id为3的unit
- 返回值
  - 无返回值，返回状态码204

##### 批量修改单位为标杆单位或非标杆单位

- url: http://127.0.0.1:8000/apps/unit/change_unit_standard/

- 请求方式PUT

- 请求参数

  ```python
  {
  	"unit_names": ["吉利集团", "利丰集团"], # 列表形式，包含企业名称
  	"state": "to_standard"  # 一个动作标识，标识置为标杆（to_standard）或(not_standard)置为非标杆
  }
  ```

- 返回参数

  ```python
  {
      "success": "单位[['吉利集团', '利丰集团']]已经全部置为标杆单位"
  }
  ```

##### 获取所有的标杆单位

- url: http://127.0.0.1:8000/apps/unit/get_standard_units/

- 请求方式GET

- 无请求参数

- 返回参数

  ```python
  [
      {
          "id": 1,
          "unit_name": "吉利集团",
          "unit_category": 1,
          "unit_status": 1,
          "unit_address": "大学科技园",
          "unit_principal": "章主任",
          "unit_phone": "13959710098",
          "standard": true,
          "created_time": "2019-12-17T04:08:36.675506Z",
          "updated_time": "2019-12-17T04:08:36.675944Z",
          "active": true,
          "memo": null,
          "traffic_permits": [  # 单位名下的通行证，一并返回，没有会返回空列表
              {
                  "id": 6,
                  "unit": {
                      "id": 1,
                      "unit_name": "吉利集团",
                      "unit_category": 1,
                      "unit_status": 1,
                      "unit_address": "大学科技园",
                      "unit_principal": "章主任",
                      "unit_phone": "13959710098",
                      "standard": true,
                      "created_time": "2019-12-17T04:08:36.675506Z",
                      "updated_time": "2019-12-17T04:08:36.675944Z",
                      "active": true,
                      "memo": null
                  },
                  "driver_name": "齐齐",
                  "driver_license_number": "412726199903010089",
                  "driver_phone": "13700291187",
                  "vehicle_number": "豫A22136",
                  "vehicle_plate_color": 2,
                  "vehicle_category": 3,
                  "vehicle_mass": 331,
                  "traffic_permit_category": 2,
                  "start_point": null,
                  "end_point": null,
                  "via_point": null,
                  "transit_start_time": 10,
                  "transit_end_time": 11,
                  "validity_category": 3,
                  "effective_time": "2019-12-17T04:14:29.630609Z",
                  "route_change_times": 3,
                  "register_channel": 2,
                  "traffic_permit_status": 1,
                  "created_time": "2019-12-17T04:14:29.630640Z",
                  "updated_time": "2019-12-17T04:14:29.630652Z",
                  "active": true,
                  "memo": null,
                  "get_vehicle_plate_color_display": "蓝牌",
                  "get_vehicle_category_display": "小型货车",
                  "get_traffic_permit_category_display": "海产品运输",
                  "get_validity_category_display": "一个月",
                  "get_register_channel_display": "PC端",
                  "get_traffic_permit_status_display": "正常"
              }
          ],
          "get_unit_category_display": "国营单位",
          "get_unit_status_display": "正常"
      },
      {
          "id": 2,
          "unit_name": "利丰集团",
          "unit_category": 2,
          "unit_status": 1,
          "unit_address": "长椿街",
          "unit_principal": "刘主任",
          "unit_phone": "13700297710",
          "standard": true,
          "created_time": "2019-12-17T04:09:25.657147Z",
          "updated_time": "2019-12-17T04:09:25.657179Z",
          "active": true,
          "memo": null,
          "traffic_permits": [],
          "get_unit_category_display": "私营单位",
          "get_unit_status_display": "正常"
      }
  ]
  ```

##### 解冻标杆单位下的所有车辆

- url: http://127.0.0.1:8000/apps/unit/unfreeze_traffic_permit/
- 请求方法PUT
- 无请求参数
- 无返回值，返回状态值200

#### TrafficPermit

##### 新增一个通行证

- url: http://127.0.0.1:8000/apps/traffic_permit/

- 请求方式POST

- 请求参数

  ```python
  {
  	"driver_name": "李天",  # 驾驶人姓名
  	"driver_license_number": "412726199303038866",  # 驾驶人驾驶证号
  	"driver_phone": "13839434366",  # 驾驶人电话
  	"vehicle_number": "豫A12211",  # 车牌号码
  	"vehicle_plate_color": 1,  # 车牌颜色，db记录数字映射可读信息
  	"vehicle_category": 1,  # 车辆种类， db记录数字映射可读信息
  	"vehicle_mass": 1121,  # 车辆重量
  	"traffic_permit_category": 1,  # 通行证种类， db记录数字映射可读信息
  	"transit_start_time": 9,  # 起始通行时间，db记录数字映射可读信息
  	"transit_end_time": 11,  # 截止通行时间， db记录数字映射可读信息
  	"validity_category": 3,  # 通行证有效期类型， db记录数字映射可读信息
  	"register_channel": 2,  # 注册渠道， db记录数字映射可读信息
  	"unit": 2  # 所属单位，可以缺省不填，以null形式存入db
  }
  ```

- 返回参数

  ```python
  {
      "id": 8,
      "unit": null,
      "driver_name": "李天",
      "driver_license_number": "412726199303038866",
      "driver_phone": "13839434366",
      "vehicle_number": "豫A12211",
      "vehicle_plate_color": 1,
      "vehicle_category": 1,
      "vehicle_mass": 1121,
      "traffic_permit_category": 1,
      "start_point": null,  # 暂时缺省
      "end_point": null,   # 暂时缺省
      "via_point": null,   # 暂时缺省
      "transit_start_time": 9,
      "transit_end_time": 11,
      "validity_category": 3,
      "effective_time": "2019-12-18T09:18:04.400746Z",  # 通行证生效时间，默认是创建记录时间
      "route_change_times": 3,  # 通行证剩余修改线路次数，默认3次
      "register_channel": 2,
      "traffic_permit_status": 1,  # 通行证状态 默认1 正常
      "created_time": "2019-12-18T09:18:04.400883Z",
      "updated_time": "2019-12-18T09:18:04.400899Z",
      "active": true,  # 数据有效性
      "memo": null,
      "get_vehicle_plate_color_display": "黄牌",  # 下面为部分字段的可读形态
      "get_vehicle_category_display": "小型客车",
      "get_traffic_permit_category_display": "危险品运输",
      "get_validity_category_display": "一个月",
      "get_register_channel_display": "PC端",
      "get_traffic_permit_status_display": "正常"
  }
  ```

##### 获取所有通行证

- url: http://127.0.0.1:8000/apps/traffic_permit/

- 请求方式GET

- 无请求参数

- 返回值

  ```python
  [
      {
          "id": 6,
          "unit": {  # 若通行证有归属单位，则展示单位信息
              "id": 1,
              "unit_name": "吉利集团",
              "unit_category": 1,
              "unit_status": 1,
              "unit_address": "大学科技园",
              "unit_principal": "章主任",
              "unit_phone": "13959710098",
              "standard": true,
              "created_time": "2019-12-17T04:08:36.675506Z",
              "updated_time": "2019-12-17T04:08:36.675944Z",
              "active": true,
              "memo": null
          },
          "driver_name": "齐齐",
          "driver_license_number": "412726199903010089",
          "driver_phone": "13700291187",
          "vehicle_number": "豫A22136",
          "vehicle_plate_color": 2,
          "vehicle_category": 3,
          "vehicle_mass": 331,
          "traffic_permit_category": 2,
          "start_point": null,
          "end_point": null,
          "via_point": null,
          "transit_start_time": 10,
          "transit_end_time": 11,
          "validity_category": 3,
          "effective_time": "2019-12-17T04:14:29.630609Z",
          "route_change_times": 3,
          "register_channel": 2,
          "traffic_permit_status": 1,
          "created_time": "2019-12-17T04:14:29.630640Z",
          "updated_time": "2019-12-17T04:14:29.630652Z",
          "active": true,
          "memo": null,
          "get_vehicle_plate_color_display": "蓝牌",
          "get_vehicle_category_display": "小型货车",
          "get_traffic_permit_category_display": "海产品运输",
          "get_validity_category_display": "一个月",
          "get_register_channel_display": "PC端",
          "get_traffic_permit_status_display": "正常"
      },
      {
          "id": 7,
          "unit": null,
          "driver_name": "乐乐",
          "driver_license_number": "412728199601038899",
          "driver_phone": "13525561172",
          "vehicle_number": "豫A17809",
          "vehicle_plate_color": 1,
          "vehicle_category": 3,
          "vehicle_mass": 331,
          "traffic_permit_category": 2,
          "start_point": null,
          "end_point": null,
          "via_point": null,
          "transit_start_time": 10,
          "transit_end_time": 11,
          "validity_category": 3,
          "effective_time": "2019-12-17T04:17:08.926210Z",
          "route_change_times": 3,
          "register_channel": 2,
          "traffic_permit_status": 1,
          "created_time": "2019-12-17T04:17:08.926258Z",
          "updated_time": "2019-12-17T04:17:08.926272Z",
          "active": true,
          "memo": null,
          "get_vehicle_plate_color_display": "黄牌",
          "get_vehicle_category_display": "小型货车",
          "get_traffic_permit_category_display": "海产品运输",
          "get_validity_category_display": "一个月",
          "get_register_channel_display": "PC端",
          "get_traffic_permit_status_display": "正常"
      }
  ]
  ```

##### 获取一个指定通行证

- url: http://127.0.0.1:8000/apps/traffic_permit/1/

- 请求方式GET

- 无请求参数，注意url中的pk值，标识获得id为1的通行证

- 返回值

  ```python
  {
      "id": 1,
      "unit": null,
      "driver_name": "刘海",
      "driver_license_number": "412726199901011123",
      "driver_phone": "13503941128",
      "vehicle_number": "豫A33759",
      "vehicle_plate_color": 1,
      "vehicle_category": 1,
      "vehicle_mass": 309,
      "traffic_permit_category": 1,
      "start_point": null,
      "end_point": null,
      "via_point": null,
      "transit_start_time": 10,
      "transit_end_time": 11,
      "validity_category": 1,
      "effective_time": "2019-12-17T02:07:53.492855Z",
      "route_change_times": 3,
      "register_channel": 1,
      "traffic_permit_status": 1,
      "created_time": "2019-12-17T02:07:53.492939Z",
      "updated_time": "2019-12-17T02:07:53.492957Z",
      "active": true,
      "memo": null,
      "get_vehicle_plate_color_display": "黄牌",
      "get_vehicle_category_display": "小型客车",
      "get_traffic_permit_category_display": "危险品运输",
      "get_validity_category_display": "一天",
      "get_register_channel_display": "微信端",
      "get_traffic_permit_status_display": "正常"
  }
  ```

##### 完整修改一个通行证

- url: http://127.0.0.1:8000/apps/traffic_permit/3/
- 请求方式PUT
- 请求参数同POST，但性质视为完整替换一个已存在的资源，此处为修改id为3的通行证
- 返回参数为修改后的通行证信息

##### 部分修改一个通行证

- url: http://127.0.0.1:8000/apps/traffic_permit/3/
- 请求方式PATCH
- 请求参数为该实例的某些属性
- 返回值为修改后的该实例的信息

##### 删除一个通行证

- url: http://127.0.0.1:8000/apps/traffic_permit/3/
- 请求方式DELETE
- 无请求参数，但注意url中的pk值，此处为3，标识删除id为3的通行证

#### TrafficPermitCategoryTransitTimeRel（通行证种类与通行时间关联表，以下简称rel）

##### 新增一个rel

- url: http://127.0.0.1:8000/apps/tp_transit_time/

- 请求方式POST

- 请求参数

  ```python
  {
  	"traffic_permit_category": 2,  # 通行证类型，db存储数字映射可读信息
  	"transit_start_time": 13,  # 准许通行开始时间，db存储数字映射可读信息
  	"transit_end_time": 18  # 准许通行截止时间，db存储数字映射可读信息
  }
  ```

- 返回参数

  ```python
  {
      "id": 2,  # rel id值
      "traffic_permit_category": 2,  # 记录的通行证种类
      "transit_start_time": 13,  # 记录的通行证种类对应的准许通行开始时间
      "transit_end_time": 18,  # 记录的通行证种类对应的准许通行截止时间
      "created_time": "2019-12-18T09:35:05.832975Z",
      "updated_time": "2019-12-18T09:35:05.833020Z",
      "active": true,  # 数据有效性
      "memo": null,  # 数据备注信息
      "get_traffic_permit_category_display": "海产品运输",  # 以下为部分字段的可读形态
      "get_transit_start_time_display": "13:00:00",
      "get_transit_end_time_display": "18:00:00"
  }
  ```

##### 获得所有rel

- url: http://127.0.0.1:8000/apps/tp_transit_time/

- 请求方式GET

- 无请求参数

- 返回参数

  ```python
  [
      {
          "id": 1,
          "traffic_permit_category": 1,
          "transit_start_time": 8,
          "transit_end_time": 12,
          "created_time": "2019-12-17T07:07:20.385945Z",
          "updated_time": "2019-12-17T07:07:20.386060Z",
          "active": true,
          "memo": null,
          "get_traffic_permit_category_display": "危险品运输",
          "get_transit_start_time_display": "08:00:00",
          "get_transit_end_time_display": "12:00:00"
      },
      {
          "id": 2,
          "traffic_permit_category": 2,
          "transit_start_time": 13,
          "transit_end_time": 18,
          "created_time": "2019-12-18T09:35:05.832975Z",
          "updated_time": "2019-12-18T09:35:05.833020Z",
          "active": true,
          "memo": null,
          "get_traffic_permit_category_display": "海产品运输",
          "get_transit_start_time_display": "13:00:00",
          "get_transit_end_time_display": "18:00:00"
      }
  ]
  ```

##### 获取一个指定的rel

- url: http://127.0.0.1:8000/apps/tp_transit_time/1/

- 请求方式GET

- 无请求参数，注意url中的pk值，标识获得id为1的rel

- 返回值

  ```python
  {
      "id": 1,
      "traffic_permit_category": 1,
      "transit_start_time": 8,
      "transit_end_time": 12,
      "created_time": "2019-12-17T07:07:20.385945Z",
      "updated_time": "2019-12-17T07:07:20.386060Z",
      "active": true,
      "memo": null,
      "get_traffic_permit_category_display": "危险品运输",
      "get_transit_start_time_display": "08:00:00",
      "get_transit_end_time_display": "12:00:00"
  }
  ```

##### 完整修改一个rel

- url: http://127.0.0.1:8000/apps/tp_transit_time/1/
- 请求方式PUT
- 请求参数同POST， 但性质视为完整修改一个已存在的资源，而非新增
- 返回值为修改后的rel信息

##### 部分修改一个rel

- url: http://127.0.0.1:8000/apps/tp_transit_time/1/
- 请求方式PATCH
- 请求参数为该实例的任意属性，不存在的属性会被忽略
- 返回值为修改后的rel信息

##### 删除一个rel

- url: http://127.0.0.1:8000/apps/tp_transit_time/1/
- 请求方式DELETE
- 无请求参数，注意url中的pk值，此处标识删除id为1的rel
- 无返回值，返回204状态码