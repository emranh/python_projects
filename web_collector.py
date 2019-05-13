#!/usr/bin/python

import urllib2
import urllib
from HTMLParser import HTMLParser

class MyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links=[]
        self.href=[]
        self.fields_name=[]
        self.fields_type=[]
    def handle_starttag(self,tag,attrs):
        if tag=="a":
            for name,value in attrs:
                if name=="href":
                    self.links.append(value)
        elif tag=="link":
            for name,value in attrs:
                if name=="href":
                    self.href.append(value)
        elif tag=="input":
            for name,value in attrs:
                if name=="name" or name=="type":
                    if name=="name":
                        self.fields_name.append(value)
                    elif name=="type":
                        self.fields_type.append(value)
    def handle_data(self,data):
        pass
    def handle_endtag(self,tag):
        pass

print """\033[1;32;40m
        +_+_+_+_+_+_+_+_++_+_+_+_+_+_+_+_Web_Collector$Author:EmranHattab_+_+_+_+_+_+_+_+__+__+__+_+_+_+_+\033[0m
        """
target=raw_input("Enter your Target please e.g :https://www.A.com : ")
p=MyParser()
url=urllib.urlopen(str(target).strip())

data=url.read()
headers=url.info()

print "-"*30,"\033[1;36;40mheaders info\033[0m","-"*30
print headers
p.feed(data)
print "\n\n\n"

print "\033[1;35;40m " ,"-"*20,"Links","-"*20,"\033[0m"
for i in range(len(p.links)):
    print p.links[i]
if len(p.links) == 0:
    print "No links founds!"
print "\033[1;33;40m " ,"-"*20,"href links","-"*20,"\033[0m"

for i in range(len(p.href)):
    print p.href[i]

if len(p.href) == 0:
    print "No href links founds!"
print "\033[1;35;40m " ,"-"*20,"form fields name","-"*20,"\033[0m"

val1=''
val2=''
n=15
print "Field Name",10*" ","Field Type"
for i in  range(len(p.fields_type)):
    try:  
        val1=p.fields_name.pop()
        val2=p.fields_type.pop()
        if len(val1)+n==20 :
            print val1,n*" ",val2
        elif len(val1)+n >20 :
            print val1,(n-((len(val1)+n)-20))*" ",val2
        else:
            print val1,(n+(20-(len(val1)+n))),val2
    except Exception ,e:
        pass


