#coding=gbk
import re
import os
import urllib.parse
import shutil

#duqu shuju 

class seqNode:
    def __init__(self):
        self.ID = ''
        self.name= ""
        self.ch_name = ""
    def show(self):
        print(self.ID+" "+self.ch_name+' '+self.name+" ")
        print('\n')
    def geturl(self):
        return "https://leetcode-cn.com/problems/" + self.name 

data ={}

def readData(data):
    l = []
    with open('abc.txt', 'r') as f:
        l =f.readlines()
        for i in l:
            i.rstrip()
            ll = i.split('|')
            node = seqNode()
            node.ID = ll[0]
            node.name = ll[1]
            node.ch_name = ll[2]
            #node.show()
            data[node.ID.strip()] =  node

def getdirname(idx):
    idx =int(idx)
    idx = int(idx/100)
    pathname = str(idx*100)+"~"+str((idx+1)*100)
    return pathname


readData(data)
cwd = os.getcwd()



getName =input("���������")
getName = getName.strip()
title = data[getName].ch_name.replace(' ','_').rstrip()

idxDirName = getdirname(getName)
print(idxDirName)
dirname = os.path.join(cwd,idxDirName)
newpath = '['+ getName.zfill(4) + ']' +title
dirname = os.path.join(dirname,newpath)


if os.path.isdir(dirname):
   print("the dir has excited")
else :
    print("���ڽ�������Ŀ¼��")
    print(dirname)
    os.mkdir(dirname)
    filename = os.path.join(dirname,title+'.md')
    print(filename)
    F =open(filename,'x')
    F.write("![](https://github.com/Sologala/SomeThings/blob/master/face.jpg?raw=true)\n")
    F.write("/*\n")
    F.write("    Sologala   @github    https://github.com/Sologala/LeetCode.git\n")
    F.write("    LeetCode   ")
    F.write(data[getName].ch_name +'   |    ' +data[getName].name+'\n')
    F.write("\n*/\n")
    F.write("\n\n\n##**˼·��** \n\n### **ac_code**\n```c\n\n```")
    F.close()
    os.system("typora "+filename)
