# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 00:51:17 2017

@author: Nehal
"""
import math

with open('INPUT.txt') as f:
    data = f.readlines()
 
for line in data:
    words = line.split()   # words contains IP,Prefix,Subnet_no
    
Ip = [x.strip() for x in words[0].split('.')]
Prefix = int(words[1])
No_of_subnets=int(words[2])
Totalno_of_address = 2**(32-Prefix)

Each_subnet_address=Totalno_of_address/int(No_of_subnets)
new_prefix = Prefix + (math.log(Totalno_of_address/Each_subnet_address)/math.log(2))
startip=((int(Ip[0]) << 24) + (int(Ip[1]) << 16) + (int(Ip[2]) << 8) + int(Ip[3]))

startip=startip-int(Each_subnet_address)
Each_subnet_last=Each_subnet_address-1

with open('OUTPUT.txt', 'w') as f:
    print('Given IP address:',words[0], file=f)
    print('Given Prefix:',words[1], file=f)
    print('Given No of subnets to be created:',words[2], file=f)
    print("New prefix created is:",new_prefix,file=f)
    print("",file=f)

for i in range(0,No_of_subnets):
    startip=startip+int(Each_subnet_address)
    b="{0:b}".format(startip).zfill(32)
    c=list(map(''.join, zip(*[iter(b)]*8)))
    with open('C:/Users/Nehal/Desktop/ACN pracs/OUTPUT.txt', 'a') as f:
        print("Subnet",i+1,"Start : ",end="",file=f)
        for j in range(0,4):
            print(int(c[j],2),end=".",file=f)
        print("\n",end="",file=f)

        endip=startip+int(Each_subnet_last)
        b="{0:b}".format(endip).zfill(32)
        c=list(map(''.join, zip(*[iter(b)]*8)))
        print("Subnet",i+1,"End : ",end="",file=f)
                
        for k in range(0,4):
            print(int(c[k],2),end=".",file=f)
        print("\n",file=f)
print("All Done! CHECK THE OUTPUT FILE")

