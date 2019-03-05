import re
import os
import urllib.parse
getName =input("请输入需要创建的工程名字");
oriName =getName;
splitres = getName.split('.',1);
idx =splitres[0].zfill(3);
getName ="["+idx+"]__"+splitres[1].replace(' ','_')
print(getName)
pathname =os.getcwd()+'/'+getName
if os.path.isdir(pathname):
   print("the dir has excited")
else :
   print("将在建立以下目录：")
   print(pathname)
   os.mkdir(pathname)
   filename =pathname+'/'+getName+'.md'
   F =open(filename,'x')
   F.write("![](https://github.com/Sologala/SomeThings/blob/master/face.jpg?raw=true)\n")
   F.write("/*\n")
   F.write("    Sologala   @github    https://github.com/Sologala/LeetCode.git\n")
   F.write("    LeetCode   ")
   F.write(oriName)
   F.write("\n*/\n")
   encodeName =urllib.parse.quote(getName);
   pic =	"[](https://github.com/Sologala/LeetCode/blob/master/"+encodeName+"/"+encodeName+".assets/0.png?raw=true)\n"
   F.write(pic)
   F.write("\n\n\n##**思路：** \n\n### **ac_code**\n```c\n\n```")
   F.close()