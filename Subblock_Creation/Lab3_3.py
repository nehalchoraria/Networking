# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 14:26:40 2017

@author: Nehal
"""
import math
with open('INPUT1.txt') as f:
    data = f.readlines()
data=list(map(lambda x:x.strip(),data))
words = data[0].split(" ")    # words contains IP,Prefix,No_of_subblocks
Ip = [x.strip() for x in words[0].split('.')]     #Contains IP address                  
Prefix = int(words[1])                            #Contains No of subblocks
No_of_subblocks=int(words[2])
Subblock_range=data[1:]                           #All subblock sizes

Totalno_of_address = 2**(32-Prefix)
startip=((int(Ip[0]) << 24) + (int(Ip[1]) << 16) + (int(Ip[2]) << 8) + int(Ip[3]))    #Ip to equivalent Integer
endip=startip
finalendip=startip+Totalno_of_address-1           # last IP address possible

z=[0 for i in range(4)]
finalendip="{0:b}".format(finalendip).zfill(32)
finalendip=list(map(''.join, zip(*[iter(finalendip)]*8))) 
for j in range(0,4):
    z[j]=int(finalendip[j],2)                     # IP in Integer form

with open('OUTPUT1.txt', 'w') as f:
    print('Given Block Address:',words[0], file=f)
    print('Given Prefix:',words[1], file=f)
    print('Given No of subblocks to be created:',words[2], file=f)
    print("",file=f)
    
for i in range(0,len(Subblock_range)):
    power=1
    sub=int(Subblock_range[i])
    while(power<sub):
        power=power*2;                               #Finding closest 2^N power
    Newprefix=Prefix+(math.log(Totalno_of_address/power)/math.log(2))
    unused=power-int(Subblock_range[i])              #Unused addresses in subblock
    endip=endip+power                                
    startip=endip-power
    b="{0:b}".format(startip).zfill(32)
    c=list(map(''.join, zip(*[iter(b)]*8)))          #Breaking into 4 parts
    with open('C:/Users/Nehal/Desktop/ACN pracs/OUTPUT1.txt', 'a') as f:
        print("New prefix :",Newprefix,file=f)
        print("Subblock",i+1,"Range : ",end="",file=f)
        for j in range(0,4):
            print(int(c[j],2),end=".",file=f)
        
        b="{0:b}".format(endip-1).zfill(32)
        c=list(map(''.join, zip(*[iter(b)]*8)))
        print("-",end="",file=f)
        for j in range(0,4):
            print(int(c[j],2),end=".",file=f)
        print("\n",end="",file=f)
        print("Subblock size is :",power,"addresses",file=f)
        print ("Unused address in subblock :",unused,file=f)
        print("",file=f)
        
a=0
n=24
with open('C:/Users/Nehal/Desktop/ACN pracs/OUTPUT1.txt', 'a') as f:
    for j in range(0,4):
        a=a+( (int(z[j]) << n ) - (int(c[j],2) << n) )       #Total addresses - Last address
        n=n-8
    print("Reserved addresses :",a,file=f)
    
print("All Done! Check the Output File!")







