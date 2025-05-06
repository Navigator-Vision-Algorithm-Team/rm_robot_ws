# RoboMaster CAN总线控制系统

基于ROS 2的机器人CAN总线硬件接口和控制系统。

## 功能包说明

- **rm_can_hardware_interface**: CAN总线硬件接口实现
- **rm_can_bringup**: 启动配置和示例

## 模块化结构

该项目采用模块化结构设计，每个功能包都保持独立，具有明确的职责边界：

- 硬件接口专注于底层CAN通信
- bringup包含启动配置和示例
- 元包组织所有相关包

## 快速开始

```bash
cd ~/rm_robot_ws
colcon build
source install/setup.bash
ros2 launch rm_can_bringup bringup.launch.py
```

## 文档

详细文档请参见 [docs](./docs) 目录。
