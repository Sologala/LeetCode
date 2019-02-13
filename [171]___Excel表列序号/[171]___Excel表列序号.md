![](https://github.com/Sologala/SomeThings/blob/master/face.jpg?raw=true)
/*
    Sologala   @github    https://github.com/Sologala/LeetCode.git
    LeetCode   171. Excel表列序号
*/给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

```
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
```

**示例 1:**

```
输入: "A"
输出: 1
```



## **思路：**

​	进制转换，没啥好说的。这里用long 是因为 有一个点会造成ret 越界

### **ac_code**
```c
class Solution {
public:
    int titleToNumber(string s) {
        long ret =0;
        for(int i=0;i<s.length();++i){
            ret = ret*26 + s[i] -'A'+1;
        }
        return ret;
    }
};
```