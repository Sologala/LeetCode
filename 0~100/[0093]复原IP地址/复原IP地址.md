![face.jpg](https://pic.leetcode-cn.com/5f44c38cfca16ba4f3886e1c9e298c5ab18a215dc25e965ec357a430e783b3af-face.jpg)

/*
[@Github _ Sologala](https://github.com/Sologala/LeetCode.git)

[`93`]**复原IP地址**|**restore-ip-addresses**

*/



## **Solution** 

分割IP地址，实际上是一个搜索问题，条件就是当前字符串表示的数字在$0 \leq x \leq 255$ 之内，可以采取分割，在接着搜索，知道分割出==4== 个满足要求的ip 地址。

#### 可以做的剪枝

1. 判断当前搜索之后剩余长度 $len(s) - i - 1 > 3 * (4 - len(已经解析的数字))  $,如果后面的长度比最坏情况（后面的几个数字都是长度为3的还要长，那么一定会出现分割剩余的情况。）

### **ac_code**
```python
class Solution:
    gs = []
    res = []
    def dfs(self,s ,i):
        if len(self.gs) >= 4:
            if i >= len(s):
                # sepreate sentence
                self.res.append('.'.join(self.gs)) 
            return
        num = 0
        for j in range(i, len(s)):
            n = ord(s[j]) - ord('0')
            if (4 - len(self.gs)) * 3 < len(s) - j - 1:
                break
            if  num * 10 + n <= 255:
                num = num * 10 + n
                self.gs.append(str(num))
                self.dfs(s, j+1)
                self.gs.pop()
                if num == 0:
                    break
            else:
                break

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.gs = []
        self.res = []
        self.dfs(s, 0)
        return self.res
```