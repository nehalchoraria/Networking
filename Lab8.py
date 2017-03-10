# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 14:54:27 2017

@author: Nehal
"""

import numpy as np
from tabulate import tabulate
import random

no_of_packets=input("Enter the number of packets: ")
no_of_packets=int(no_of_packets)

array=np.zeros((no_of_packets,6))
array=array.astype(int)

for i in range(0,no_of_packets):
    packetno=i
    arrival_time=random.randint(0,50)
    service_time=5
    priority=random.randint(1,9)
    newrow=[packetno,arrival_time,service_time,priority,0,0]
    array[i]=newrow
    #x = np.vstack([x, newrow])

#packtno,arrivaltime,servictim,priority
print("Random array generated")
print(tabulate(array[:,:-1],headers=["Process","Arrival time","Process time","Priority","Waitingtime"]))
print()

print("Array sorted by Arrival time")
array=array[array[:,1].argsort()]
print(tabulate(array[:,:-1],headers=["Process","Arrival time","Process time","Priority","Waitingtime"]))

print()

process=""
time=int(array[0][1])

index=0   #Tracks the row of next process
next_pocess=0  #Name of the next process
next_priority=0 #Larger number has more priority
checker=0 #Checking if no process in time t? Increment by time 1

while(np.any(array[:,5]!=1)):
    if(array[0][5]!=1):
        process="P"+str(array[0][0])+" "
        time=time+int(array[0][2])
        array[0][5]=1
        array[0][4]=str(time-int(array[0][1])-int(array[0][2]))
        #print(tabulate(array[:,:-1],headers=["Process","Arrival time","Process time","Priority","Waiting time"]))

    else:
        for i in range(0,no_of_packets):
            if(time >= int(array[i][1]))&(next_priority<array[i][3])&(array[i][5]==0):
                index=i
                next_pocess=int(array[i][0])
                next_priority=int(array[i][3])
                checker=checker+1
                
        if(checker==0):
            time=time+1
            checker=0
        else:
            time=time+int(array[next_pocess][2])
            array[index][4]=str(time-int(array[index][1])-int(array[index][2]))
            array[index][5]=1
            checker=0
            process=process+"P"+str(next_pocess)+" "
            next_priority=0
            #print(process)
            #print(tabulate(array[:,:-1],headers=["Process","Arrival time","Process time","Priority","Waiting time"]))
        #print("Updated Time : "+str(time))
              
print("After priority scheduling : ")
print(tabulate(array[:,:-1],headers=["Process","Arrival time","Process time","Priority","Waitingtime"]))
print("Completion time : ",time)
print("Average Waiting time : ",(np.average(array,axis=0))[4])
