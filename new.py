#coding=utf-8
import re
import os
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
    daat = {}
    l = []
    with open('abc.txt', 'r',encoding='UTF-8') as f:
        l =f.readlines()
        for i in l:
            if len(i) == 0:
                continue
            i.rstrip()
            ll = i.split('|')
            if len(ll) < 3:
                continue
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



getName =input("Plz Input the Question idx\n")
getName = getName.strip()
if getName not in data.keys():
    EnName= input("\t没有该题的信息，请输入英文题目\n")
    ChName= input("\t没有该题的信息，请输入中文题目\n")
    with open('abc.txt', 'a+',encoding='UTF-8') as f:
        f.write('\n'+getName+' | '+EnName + '|' + ChName+'\n')
    readData(data)

title = data[getName].ch_name.replace(' ','_').rstrip()

idxDirName = getdirname(getName)
print(idxDirName)
dirname = os.path.join(cwd,idxDirName)
newpath = '['+ getName.zfill(4) + ']' +title
dirname = os.path.join(dirname,newpath)

filename = os.path.join(dirname,title+'.md')
if os.path.isdir(dirname):
   print("the dir has excited")
else :
    print("Creating the dir as follow:")
    os.mkdir(dirname)
    F =open(filename,'x',encoding='UTF-8')
    F.write("![face.jpg](https://pic.leetcode-cn.com/5f44c38cfca16ba4f3886e1c9e298c5ab18a215dc25e965ec357a430e783b3af-face.jpg)\n\n")
    F.write("/*\n")
    F.write('[@Github _ Sologala](https://github.com/Sologala/LeetCode.git)\n\n')
    print(data[getName].ch_name +'     |    ' +data[getName].name)
    F.write("[`"+getName+'`]**'+data[getName].ch_name.strip()+'**|**' +data[getName].name.strip()+'**\n')
    F.write("\n*/\n")
    F.write("\n\n\n## **Solution** \n\n### **ac_code**\n```c\n\n```")
    F.close()
os.system("typora "+filename)
