#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random
import rospy
from std_msgs.msg import Int32
from mypkg.msg import money

#pub_topic_msg
angleCount=2
angle = list(range(0, angleCount))
angle[1]=[0,1,2,3]
angle[0]=[0,1,0,1]

#user_number
def select(ration):
    if(ration==2):
        number=int(input("blue:1 red:2\n"))
    elif(ration==4):
        number=int(input("1~4?\n"))
    return number-1
   
#random_num
def random_num(ration):
    count=random.randint(0,3)
    if(ration==2):
        return angle[0][count]
    elif(ration==4):
        return angle[1][count]

#pub1_topic_msg.salary
def judge(ration,salary,ru_num,user_num):
    if ru_num==user_num:
        return ration*salary
    else:
        return 0


if __name__ == '__main__': 
   rospy.init_node('sevice_client')
   pub=rospy.Publisher('angle_send',Int32,queue_size=1)
   pub1=rospy.Publisher('result',money,queue_size=1)
   rate=rospy.Rate(10)

   #user_input and judging
   ration = int(input("2?4?\n"))
   salary= int(input("How much bet?\n"))
   user_num=select(ration)
   ru_num=random_num(ration)
   money1=judge(ration,salary,ru_num,user_num)

   print(ration,salary,user_num,ru_num,money1) #answer

   #pun2_topic_msg.result
   msg=money()
   if money1==0:
         msg.result="loooooser!!!!!"
   else:
         msg.result="win!win!win!"
   msg.salary=money1

   #forは非同期に対応させるため
   for i in range(1): 
       pub.publish(ru_num)
       for i in range(3):
           pub1.publish(msg)
           rate.sleep()
