![](https://github.com/Sologala/SomeThings/blob/master/face.jpg?raw=true)
/*
    Sologala   @github    https://github.com/Sologala/LeetCode.git
    LeetCode   N皇后 II
   |     n-queens-ii

*/

*n* 皇后问题研究的是如何将 *n* 个皇后放置在 *n*×*n* 的棋盘上，并且使皇后彼此之间不能相互攻击。

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/8-queens.png)

上图为 8 皇后问题的一种解法。

给定一个整数 *n*，返回 *n* 皇后不同的解决方案的数量。

**示例:**

```
输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
```

##**Solution** 

这道题和 N皇后的算法一样 ，只不过我们不需要那个 res 数组来存储了，只需要用一个计数记录一下 每一种解法就行了。

### **ac_code**
```c
class Solution {
public:
    int cnt = 0;
    int N;
    unordered_map<int,int> vis[3];
    void dfs(int idx){
        if(idx==N){
            cnt++;
            return;
        }
        for(int i = 0;i<N;++i){
            int b1,b2;
            b1 = idx+i;
            b2 = idx-i;
            if(vis[0][i]==0&&vis[1][b1]==0&&vis[2][b2]==0){
                vis[0][i]=1;
                vis[1][b1]=1;
                vis[2][b2]=1;
                dfs(idx+1);
                vis[0][i]=0;
                vis[1][b1]=0;
                vis[2][b2]=0;
            }
        }
    }
    int totalNQueens(int n) {
        N = n;
        dfs(0);
        return cnt;
    }
};
```