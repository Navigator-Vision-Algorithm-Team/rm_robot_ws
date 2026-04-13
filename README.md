# RoboMaster CAN 总线控制系统

基于 ROS 2 的 RoboMaster 机器人 CAN 总线硬件接口与控制系统，支持大疆 2006 / 3508 / 6020 系列电机，集成 ros2_control 控制栈与 Mecanum 轮底盘键盘遥控。

## 仓库地址

[https://github.com/Navigator-Vision-Algorithm-Team/rm_robot_ws](https://github.com/Navigator-Vision-Algorithm-Team/rm_robot_ws)

## 子模块

| 子模块 | 路径 | 说明 |
|--------|------|------|
| [rm_can_hardware_interface](https://github.com/Navigator-Vision-Algorithm-Team/rm_can_hardware_interface) | `src/rm_can_hardware_interface` | ros2_control CAN 总线硬件接口实现 |
| [rm_can_bringup](https://github.com/Navigator-Vision-Algorithm-Team/rm_can_bringup) | `src/rm_can_bringup` | 启动配置、控制器参数与 URDF 描述 |
| [cakey_model](https://github.com/Navigator-Vision-Algorithm-Team/cakey_model) | `src/cakey_model` | 机器人 URDF/Xacro 模型与 STL 网格 |
| [units](https://github.com/Navigator-Vision-Algorithm-Team/units) | `src/units` | nholthaus/units C++ 物理单位库（头文件包装） |

## 克隆仓库

本仓库包含 Git 子模块，克隆时需同步子模块代码。

**推荐方式（一步到位）：**

```bash
git clone --recurse-submodules https://github.com/Navigator-Vision-Algorithm-Team/rm_robot_ws.git
```

**若已克隆但未同步子模块：**

```bash
cd rm_robot_ws
git submodule update --init --recursive
```

**后续更新子模块到最新提交：**

```bash
git submodule update --remote --merge
```

## 环境依赖

- ROS 2 Humble（或更高版本）
- `ros2_control` / `ros2_controllers`
- SocketCAN 驱动（`can-utils`）
- Python 3（用于键盘遥控脚本）

## 快速开始

### 1. 配置 CAN 接口

手动启动 CAN0（波特率 1 Mbps）：

```bash
sudo ip link set can0 type can bitrate 1000000
sudo ip link set can0 up
```

或使用自动启动脚本（需要 root 权限）：

```bash
sudo src/rm_can_hardware_interface/setup_can0_autostart.sh
```

### 2. 构建工作空间

```bash
cd ~/rm_robot_ws
colcon build
source install/setup.bash
```

### 3. 启动控制系统

```bash
ros2 launch rm_can_bringup rrbot.launch.py
```

### 4. 键盘遥控（Mecanum 底盘）

在另一个终端运行：

```bash
python3 keyboard_teleop.py
```

键位说明：

```
   q    w    e
   a    s    d
        x

w/s : 前进 / 后退
a/d : 左平移 / 右平移
q/e : 左转 / 右转
x   : 急停
Ctrl-C : 退出
```

## 目录结构

```
rm_robot_ws/
├── src/
│   ├── rm_can_hardware_interface/  # CAN 硬件接口（子模块）
│   ├── rm_can_bringup/             # 启动配置（子模块）
│   ├── cakey_model/                # 机器人模型（子模块）
│   └── units/                      # 物理单位库（子模块）
├── keyboard_teleop.py              # Mecanum 键盘遥控脚本
└── README.md
```

## 贡献

请参阅 [CONTRIBUTING.md](./CONTRIBUTING.md)。
