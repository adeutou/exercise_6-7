#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
from std_msgs.msg import String


def move():
	rospy.init_node('my_created_node', anonymous=True)
	#log = rospy.Publisher('chatter', String, queue_size=10)
	takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
	land = rospy.Publisher('/drone/land', Empty, queue_size=1)
	vel_publisher = rospy.Publisher('/drone/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()
	
	empty = Empty()

	speed = input("Input your speed:")
	distance = input("Type your distance:")

        takeoff.publish(empty)  
	vel_msg.linear.x = abs(speed)
   	
	vel_msg.linear.x = 0
    	vel_msg.linear.y = 0
    	vel_msg.linear.z = 10
    	vel_msg.angular.x = 0
    	vel_msg.angular.y = 0
    	vel_msg.angular.z = -1
	
	while not rospy.is_shutdown():
	     #msg = messageToRos.get()
	    # rospy.loginfo('Logging message: ',msg)
	     #log.publish(msg)
	     #Setting the current time for distance calculus
	     t0 = rospy.Time.now().to_sec()
	     current_distance = 0	
		
	     #Loop to move the drone in an specified distance
	     while(current_distance < distance):
		 
            	 #Publish the velocity
                 vel_publisher.publish(vel_msg)
                 #Takes actual time to velocity calculus
                 t1=rospy.Time.now().to_sec()
                 #Calculates distancePoseStamped
                 current_distance= speed*(t1-t0)
             #After the loop, stops the robot
             vel_msg.linear.x = 0
             #Force the robot to stop
             vel_publisher.publish(vel_msg)
	
	     land.publish(empty)
	     return
		
if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException: pass
