#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped
import sys
import select
import termios
import tty

# 键位映射
# w/x: 前进/后退
# a/d: 左平移/右平移
# q/e: 左转/右转
# s: 停止

move_bindings = {
    'a': (1.0, 0.0, 0.0),
    'd': (-1.0, 0.0, 0.0),
    'w': (0.0, 1.0, 0.0),
    's': (0.0, -1.0, 0.0),
    'q': (0.0, 0.0, 1.0),
    'e': (0.0, 0.0, -1.0),
    'x': (0.0, 0.0, 0.0),
}

msg = """
Mecanum Robot Keyboard Teleop
-----------------------------
Moving around:
   q    w    e
   a    s    d
        x

w/s : forward/backward
a/d : left/right (strafing)
q/e : turn left/right
x   : force stop

CTRL-C to quit
"""

def getKey(settings):
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def main(args=None):
    settings = termios.tcgetattr(sys.stdin)

    rclpy.init(args=args)
    node = rclpy.create_node('keyboard_teleop')
    # 当 use_stamped_vel: true 时，控制器默认监听 ~/reference 话题
    pub = node.create_publisher(TwistStamped, '/mecanum_drive_controller/reference', 10)

    speed = 10    # 线速度 m/s
    turn = 31.4   # 角速度 rad/s
    x = 0.0
    y = 0.0
    th = 0.0
    status = 0

    try:
        print(msg)
        while True:
            key = getKey(settings)
            
            if key in move_bindings.keys():
                x = move_bindings[key][0]
                y = move_bindings[key][1]
                th = move_bindings[key][2]
            elif key == '\x03': # CTRL-C
                break
            else:
                # 没有任何按键输入时，可以选择不重置速度，或者重置速度
                pass 
                
            twist = TwistStamped()
            twist.header.stamp = node.get_clock().now().to_msg()
            twist.header.frame_id = "root" 
            twist.twist.linear.x = x * speed
            twist.twist.linear.y = y * speed
            twist.twist.linear.z = 0.0
            twist.twist.angular.x = 0.0
            twist.twist.angular.y = 0.0
            twist.twist.angular.z = th * turn
            pub.publish(twist)

    except Exception as e:
        print(e)
    finally:
        twist = TwistStamped()
        twist.header.stamp = node.get_clock().now().to_msg()
        twist.twist.linear.x = 0.0
        twist.twist.linear.y = 0.0
        twist.twist.angular.z = 0.0
        pub.publish(twist)
        
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
