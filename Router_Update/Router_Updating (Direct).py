# -*- coding: utf-8 -*-
"""Created on Wed Feb  1 18:42:50 2017

@author: Nehal
"""
#Assuming Router 1 is reading router 2 table

Hop_R1 = "A.B.C.D"
Hop_R2 = "W.X.Y.Z"
with open('Router2.txt') as f:
    data = f.readlines()

#Interface=[None]*len(data)
#NextHop=[None]*len(data)
#Cost=[None]*len(data)
#Prefix=[None]*len(data)
#Ip=[None]*len(data)
#Row=[None]*len(data)    #Initialize variables
#
#i=0
#while(i<len(data)):               
#    Row[i] = [x.strip() for x in data[i].split(' ')] 
#    i=i+1
#
#i=0
#for i in range(0,2):
#    Ip[i]=Row[i][0]
#    Prefix[i]=Row[i][1]
#    Cost[i]=Row[i][2]
#    NextHop[i]=Row[i][3]
#    Interface[i]=Row[i][4]

Row=[None]*len(data)  
            
Row[1] = [x.strip() for x in data[1].split(' ')] 
print(Row[1][1])
Ip=Row[1][0]
Prefix=Row[1][1]
Cost=Row[1][2]
NextHop=Row[1][3]
Interface=Row[1][4]

Hop=data[0]
print(Hop)

Ip=[x.strip() for x in Ip.split('.')]
print(Ip[0])

print(Ip)
print(Prefix)
print(Cost)
print(NextHop)
print(Interface)



i=0
bin_mask=""
while(i<int(Prefix)):
    bin_mask=bin_mask+"1"
    i=i+1                    
bin_mask=bin_mask.ljust(32,'0')                    #mask in binary

int_mask=[0 for i in range(4)]
bin_mask=list(map(''.join, zip(*[iter(bin_mask)]*8))) 
for j in range(0,4):
    int_mask[j]=int(bin_mask[j],2)                 #mask in integer
   
net_addr=[0 for i in range(4)]
for i in range(0,4):
    net_addr[i]=int_mask[i]&int(Ip[i])
print(net_addr)                                    #Found net address

save=""
with open('Router1.txt',"r+") as f:
    for j in range(0,4):  
        save=save+str(net_addr[j])+"."
    save = save[:-1]    
    line_found = any(save in line for line in f)
    if not line_found:
        print(save,Prefix,Cost,Hop[0:len(Hop)-1],Interface,file=f)

#Reading Router table R1 By R2

with open('Router1.txt') as f:
    data = f.readlines()
    
Row=[None]*len(data)  
            
Row[1] = [x.strip() for x in data[1].split(' ')] 
Ip=Row[1][0]
Prefix=Row[1][1]
Cost=Row[1][2]
NextHop=Row[1][3]
Interface=Row[1][4]
Ip=[x.strip() for x in Ip.split('.')]

Hop1=data[0]
print("secmnd",Hop1)

i=0
bin_mask=""
while(i<int(Prefix)):
    bin_mask=bin_mask+"1"
    i=i+1                    
bin_mask=bin_mask.ljust(32,'0')                    #mask in binary

int_mask=[0 for i in range(4)]
bin_mask=list(map(''.join, zip(*[iter(bin_mask)]*8))) 
for j in range(0,4):
    int_mask[j]=int(bin_mask[j],2)                 #mask in integer
   
net_addr=[0 for i in range(4)]
for i in range(0,4):
    net_addr[i]=int_mask[i]&int(Ip[i])
print(net_addr)                                    #Found net address

save=""
with open('Router2.txt',"r+") as f:
    for j in range(0,4):  
        save=save+str(net_addr[j])+"."
    save = save[:-1]    
    line_found = any(save in line for line in f)
    if not line_found:
        print(save,Prefix,Cost,Hop1[0:len(Hop1)-1],Interface,file=f)