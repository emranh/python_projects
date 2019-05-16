#!/usr/bin/python
import urllib
import urllib2
import os
import threading
import thread
import sys
import time

print """_+_+_+_+_+_+_+_+__+_+_+_+_+_+_+WebFuZzy%Author:EmranHattab_+_+__+_+_+_+_+__+_+_+"""

listener_val=True

#stream over the file and parse it into list of lines
File=str(raw_input("Enter the file name you want to brute force please: ")).strip()
with open(File) as path:
    lines=[line.strip("\n") for line in path]

#used as tracker to stop the threads before main thread exit !
g=False
#count the number of lines existed in the file for testing process
L=str(os.popen("wc %s" % File).read())
print "#requests:",(L.strip().split())[0]

target=str(raw_input("Enter the target : ")).strip()

#reader used as thread 
def reader(): 
        global g
        global lines
        global target
        #iterate over the list line by line while the list is not empty and the g tracker not True
        while len(lines) !=0 and g !=True:
            try:
                time.sleep(0.3)
                url=str(target+"/"+str(lines.pop()).strip()).strip()
                full_path=urllib2.Request(url)
                opener=urllib2.build_opener(urllib2.HTTPCookieProcessor)
                request=opener.open(full_path)
                print request.getcode(),"ok ",url
                
            except Exception ,e :
                pass

print "press the Enter key    to stop the Fuzzer !"
time.sleep(3)


#60 threads used


threads=[]
for i in range(60):
    threads.append(threading.Thread(target=reader,args=()))

for i in range(len(threads)):
    threads[i].start()


def timer():
    global g
    global lines
    global listener_val
    future=time.time()+20
    while time.time() <future and g != True and len(lines) !=0:
        time.sleep(5)
        print "remaining:",len(lines)
        future=time.time()+20
    else:
        if len(lines) !=0:
            pass
        else:
            print "Please press the \"Enter\"  key to stop the Fuzzer"


t1=threading.Thread(target=timer,args=())
t1.start()


try :
    while  raw_input("") is None:
        time.sleep(1)
    else:
        g=True
        print "Exiting!!"
        time.sleep(15)
        print "Fuzzer has stopped successfully!"
        sys.exit(1)
except KeyboardInterrupt :
        g=True
        print "Exiting!!"
        time.sleep(15)
        print "Fuzzer has stopped successfully!"
        sys.exit(1)
 


