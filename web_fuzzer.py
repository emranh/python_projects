#!/usr/bin/python
import urllib
import urllib2
import os
import threading
import sys
import time

print """_+_+_+_+_+_+_+_+__+_+_+_+_+_+_+WebFuZzy%Author:EmranHattab_+_+__+_+_+_+_+__+_+_+"""


#stream over the file and parse it into list of lines
File=str(raw_input("Enter the file name you want to brute force please: ")).strip()
with open(File) as path:
    lines=[line for line in path]

#used as tracker to stop the threads before main thread exit !
g=False
#count the number of lines existed in the file for testing process
L=str(os.popen("wc %s" % File).read())
print "#requests:",(L.strip().split())[0]


#reader used as thread 
def reader():
        
        global g
        global lines
        #iterate over the list line by line while the list is not empty and the g tracker not True
        try:
            while lines is not [] and g !=True:
                    
                    url="https://www.facebook.com/"+str(lines.pop()).strip()
                    full_path=urllib2.Request(url)
                    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor)
                    request=opener.open(full_path)
                    print request.getcode(),"ok ",url

        except Exception ,e:
           pass

print "Press Any Key to stop the Fuzzer !"
time.sleep(3)

#15 threads used 
for t in range(15):
    t1=threading.Thread(target=reader,args=())
    t1.start()
#listening to any key to stop the threading process
while raw_input("") is None:
    pass
else:
    g=True
    time.sleep(3)
    print "Fuzzer has stopped successfully!"
    sys.exit(1)

