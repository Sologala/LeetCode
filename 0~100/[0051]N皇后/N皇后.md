![](https://github.com/Sologala/SomeThings/blob/master/face.jpg?raw=true)
/*
    Sologala   @github    https://github.com/Sologala/LeetCode.git
    LeetCode   N皇后
   |     n-queens

*/

*n* 皇后问题研究的是如何将 *n* 个皇后放置在 *n*×*n* 的棋盘上，并且使皇后彼此之间不能相互攻击。

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/8-queens.png)

上图为 8 皇后问题的一种解法。

给定一个整数 *n*，返回所有不同的 *n* 皇后问题的解决方案。

每一种解法包含一个明确的 *n* 皇后问题的棋子放置方案，该方案中 `'Q'` 和 `'.'` 分别代表了皇后和空位。

**示例:**

```
输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。
```

##**Solution** 

dfs 搜索就完事儿了 。

我们可以每一行开始搜索，`void dfs（int idx)` 遍历每一行的所有位置，观察每一个位置能否放置一个皇后。

在这里就涉及到一个检查是否合法的操作。

方便起见我这里就使用了三个 `unordered_map <int,int> vis[3]` 其中一个表示某一列能否放置。

其他两个可以使用，某一条斜线的  `y = k + b1`   `y = -x + b2` 来导出两个 `b1 b2` 并且使用这个来描述是哪一条斜线。

### **ac_code**
```c
class Solution {
public:
    vector<string> res;
    vector<vector<string>> ret;
    int N;
    unordered_map<int,int> vis[3];
    void dfs(int idx){
        if(idx==N){
            ret.push_back(res);
            return;
        }
        for(int i = 0;i<N;++i){
            int b1,b2;
            b1 = idx+i;
            b2 = idx-i;
            if(vis[0][i]==0&&vis[1][b1]==0&&vis[2][b2]==0){
                res[idx][i] = 'Q';
                vis[0][i]=1;
                vis[1][b1]=1;
                vis[2][b2]=1;
                dfs(idx+1);
                res[idx][i] = '.';
                vis[0][i]=0;
                vis[1][b1]=0;
                vis[2][b2]=0;
            }
        }
    }
    
    vector<vector<string>> solveNQueens(int n) {
        N = n;
        res = vector<string>(n,string(n,'.'));
        dfs(0);
        return ret;
    }
};
```