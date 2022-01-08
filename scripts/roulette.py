#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
import random
import time
import RPi.GPIO as GPIO
from std_msgs.msg import Int32

#PIN_set
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pin=[4,17,27,22]
for i in range(4):
    GPIO.setup(pin[i], GPIO.OUT)


detly=1/1000
count=0
v=-1
angle=[63,191,318,517,446]

#half_wave
StepCount = 8
Seq = list(range(0, StepCount))
Seq[0] = [1,0,0,1]
Seq[1] = [1,0,0,0]
Seq[2] = [1,1,0,0]
Seq[3] = [0,1,0,0]
Seq[4] = [0,1,1,0]
Seq[5] = [0,0,1,0]
Seq[6] = [0,0,1,1]
Seq[7] = [0,0,0,1]

#steping_moter_set
def setStep(w1, w2, w3, w4):
    GPIO.output(pin[0], w1)
    GPIO.output(pin[1], w2)
    GPIO.output(pin[2], w3)
    GPIO.output(pin[3], w4)

#move_set
def forward(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)

#main_fun
def rullet(message1):
    global v
    v= message1.data
    t=angle[v]
    d=510-t
    for i in range(2):
        forward(detly,510)
    forward(detly,t)
    print("戻るまで待って！")
    time.sleep(4)
    forward(detly,d)
    print(v)


if __name__ == '__main__':
    rospy.init_node('rulette_sever1')
    sub=rospy.Subscriber('angle_send',Int32,rullet)
    rospy.spin()
