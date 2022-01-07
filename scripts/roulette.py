#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
import random
import time
import RPi.GPIO as GPIO
from std_msgs.msg import Int32


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pin=[4,17,27,22]
StepCount = 8
angleCount=2
detly=1/1000
count=0
v=-1

angle=[0,90,180,270]

Seq = list(range(0, StepCount))
Seq[0] = [1,0,0,1]
Seq[1] = [1,0,0,0]
Seq[2] = [1,1,0,0]
Seq[3] = [0,1,0,0]
Seq[4] = [0,1,1,0]
Seq[5] = [0,0,1,0]
Seq[6] = [0,0,1,1]
Seq[7] = [0,0,0,1]

for i in range(4):
    GPIO.setup(pin[i], GPIO.OUT)
    
def setStep(w1, w2, w3, w4):
    GPIO.output(pin[0], w1)
    GPIO.output(pin[1], w2)
    GPIO.output(pin[2], w3)
    GPIO.output(pin[3], w4)
 
def forward(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)

def rullet(message1):
    global v
    v= message1.data
    t=angle[v]
    d=360-t
    for i in range(3):
        forward(detly,360+30)
    forward(detly,t)
    print("戻るまで待って！")
    time.sleep(4)
    forward(detly,d)
    print(v)



#pub=rospy.Publisher('rulette_sever1',Int32,queue_size=100)
#pub.publish(count)



if __name__ == '__main__':
 # rullet(1)
    rospy.init_node('rulette_sever1')
    sub=rospy.Subscriber('rullette_judge1',Int32,rullet)
    rospy.spin()
    print("r")
    
