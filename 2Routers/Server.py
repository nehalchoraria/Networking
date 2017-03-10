# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 15:01:01 2017

@author: Nehal
"""
import socket, pickle 
from tabulate import tabulate
from netaddr import IPNetwork

t = tabulate("")

newlist=[]
with open('C:/Users/Nehal/Desktop/ACN pracs/Router2.txt','r') as f:
    for line in f:
        newlist.append(line.split())     #Reaading the table

print("\n Router 2 Initially \n")
print(tabulate(newlist[1:len(newlist)],headers=["Ip Address","Prefix","Cost","Next hop","Interface"]))  #Printing table

prefix=[]
mask=[]

iter_length=len(newlist)-1;

for i in range(1,iter_length+1):
    Prefix=newlist[i][1]
    k=0
    bin_mask=""
    while(k<int(Prefix)):
        bin_mask=bin_mask+"1"
        k=k+1                    
    bin_mask=bin_mask.ljust(32,'0')                    #mask in binary
    temp=""
    bin_mask=list(map(''.join, zip(*[iter(bin_mask)]*8))) 
    for j in range(0,4):
        temp=temp+str(int(bin_mask[j],2))+"."
    mask.append(temp[0:len(temp)-1])

modified_list=[]

fixed=[[1,"Ripv2"]]
for i in range(1,len(newlist)):
    modified_list.append(["2",newlist[i][0],mask[i-1],newlist[i][3],newlist[i][2],newlist[i][4]])

print("\n Sent Packet : \n")
print(tabulate(fixed,headers=["Command   ","Version"],tablefmt="pipe"))     #Sent Data
print(tabulate( "",tablefmt="orgtbl"))
print(tabulate(modified_list,headers=["Identifier","IP Address","Mask","Next Hop","Metric","Interface"],tablefmt="pipe"))  
                                

data_string = pickle.dumps(modified_list)

HOST = 'localhost'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(1)
conn, addr = s.accept()

Nexthop=addr

data = conn.recv(4096)
data_recv = pickle.loads(data)
conn.send(data_string)
conn.close()

Net_addr=[]
Prefix=[]

for i in range(0,len(data_recv)):  
    Ip=data_recv[i][1]    
    mask=data_recv[i][2]
    
    temp="/"+mask
    Ip_with_pre = IPNetwork(Ip,temp)
    n=""+str(Ip_with_pre.prefixlen)
    n=n[n.find("@")+1:]
    Prefix.append(n)

    Ip=[x.strip() for x in Ip.split('.')]
    mask=[x.strip() for x in mask.split('.')]
    
    a=""
    for i in range(0,4):
        a=a+str(int(mask[i])&int(Ip[i]))+"."
    Net_addr.append(a[:len(a)-1])
    
t=False
for i in range(0,len(data_recv)):
    with open('C:/Users/Nehal/Desktop/ACN pracs/Router2.txt',"r+") as search:
        for line in search:
            if data_recv[i][5] in line:
                t=False
                break
            else:
                t=True
        if(t):
            print(Net_addr[i],Prefix[i],data_recv[i][4],"192.168.1.1",data_recv[i][5],file=search)

  
output=[]   
with open('C:/Users/Nehal/Desktop/ACN pracs/Router2.txt') as f:
    for line in f:
        output.append(line.split())     #Reaading the table

print("\n Router 2 After Update \n")
print(tabulate(output[1:len(output)],headers=["Ip Address","Prefix","Cost","Next hop","Interface"]))  #Printing table

