![face.jpg](https://pic.leetcode-cn.com/5f44c38cfca16ba4f3886e1c9e298c5ab18a215dc25e965ec357a430e783b3af-face.jpg)

/*
    Sologala   @github    https://github.com/Sologala/LeetCode.git

   [168]Excel表列名称
     |     excel-sheet-column-title

*/

给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
示例 1:

输入: 1
输出: "A"
示例 2:

输入: 28
输出: "AB"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-title
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## **Solution** 

​	首先这是一个 `进制转换` 问题,等同于转换成为`26` 进制.因此我们可以是用`stack`来辅助转换.但是这里涉及到一个下标问题,也就是我们在`%26`的时候下表是 从`1` 开始的,为了能够正确的得到结果,我们先将当前的`n--` 处理一下,当然在每次循环之后也需要处理一下.不然不能得到正确的结果.

​	得到的`stack` 中的结果 `reverse` 就行了,当然我这里为了输出方便就直接用了`string`

### **ac_code**
```c
class Solution {
public:
    string convertToTitle(int n) {
        string ret;
        while(n){
            n--;
            ret.push_back(char(n%26+'A'));
            n/=26;
            
        }
        reverse(ret.begin(),ret.end());
        return ret;
    }
};
```