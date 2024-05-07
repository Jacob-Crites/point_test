#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from time import sleep
import numpy as np
from geometry_msgs.msg import Point

#Constant publishing


class Point_Test_Node(Node): #Node Class (just for program)

    def __init__(self):
        super().__init__("point_test_node") #Node name
                                             #What is typed in terminal
        self.my_point = self.create_publisher(Point, 'point', 10)
        self.get_logger().info("Publishing Fake Data")
        self.timer = self.create_timer(1.0, self.point_publish)
        

    def point_publish(self):
        fake_data = Point()
        #State 1
        fake_data.x = float(0.7)
        fake_data.z = float(0)
        self.get_logger().info("Publishing X: " + str(fake_data.x) )
        self.get_logger().info("Publishing Z: " + str(fake_data.z) )
        self.my_point.publish(fake_data)
        sleep(1)
        #State 2
        fake_data.x = float(1)
        fake_data.z = float(0.5)
        self.get_logger().info("Publishing X: " + str(fake_data.x) )
        self.get_logger().info("Publishing Z: " + str(fake_data.z) )
        self.my_point.publish(fake_data)
        sleep(1)
        #State 3
        fake_data.x = float(0.8)
        fake_data.z = float(-0.4)
        self.get_logger().info("Publishing X: " + str(fake_data.x) )
        self.get_logger().info("Publishing Z: " + str(fake_data.z) )
        self.my_point.publish(fake_data)
        sleep(1)
        #State 4
        fake_data.x = float(0.5)
        fake_data.z = float(0.5)
        self.get_logger().info("Publishing X: " + str(fake_data.x) )
        self.get_logger().info("Publishing Z: " + str(fake_data.z) )
        self.my_point.publish(fake_data)
        sleep(1)
        #State 5
        fake_data.x = float(1)
        fake_data.z = float(0)
        self.get_logger().info("Publishing X: " + str(fake_data.x) )
        self.get_logger().info("Publishing Z: " + str(fake_data.z) )
        self.my_point.publish(fake_data)
        sleep(1)
        #State 6
        fake_data.x = float(0.5)
        fake_data.z = float(0)
        self.get_logger().info("Publishing X: " + str(fake_data.x) )
        self.get_logger().info("Publishing Z: " + str(fake_data.z) )
        self.my_point.publish(fake_data)
        sleep(1)
        #State 7
        fake_data.x = float(0.3)
        fake_data.z = float(0)
        self.get_logger().info("Publishing X: " + str(fake_data.x) )
        self.get_logger().info("Publishing Z: " + str(fake_data.z) )
        self.my_point.publish(fake_data)
        sleep(2)
    
            

def main(args = None):
    rclpy.init(args=args)
    node = Point_Test_Node()
    #
    rclpy.spin(node)

    rclpy.shutdown()
if __name__ == '__main__':
    main()


"""
#One time publish
def main(args = None):
    rclpy.init(args=args)

    node = rclpy.create_node('Point_Test_Node')

    publisher = node.create_publisher(Point, "point", 10)

    msg = Point()
    send = True
    i = 1

    while rclpy.ok():
        msg.x = float(5)
        msg.z = float(3)
        i += 1
        node.get_logger().info('Publishing: "%s"' % msg)

        if send:
            publisher.publish(msg)
            Send = False
        sleep(10)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
"""
