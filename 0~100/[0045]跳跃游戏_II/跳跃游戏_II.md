![](https://github.com/Sologala/SomeThings/blob/master/face.jpg?raw=true)
/*
    Sologala   @github    https://github.com/Sologala/LeetCode.git
    LeetCode   跳跃游戏 II
   |     jump-game-ii

*/



\##**Solution**

这道题可以很简单的想到 用搜索去做，但是如果从起点到终点 直接搜索的话会超时，

所以想到用动态规划 + 贪心来做。

我们倒着从终点搜索回来，`dp[i]` 表示 从 `i` 到终点的最近的 步数。

`dp[i] = 1 + min{ dp[i+1] , dp[i+2] , dp[i+3] ....... dp[nums.size()-1]}`

也就是当前`i` 位置可以去的最短的一个路径。

这里可以进行一些简单的剪纸

如果这个`num[i] == 0` 可以直接宣判这个 `dp[i] = INT_MAX` 是不能到达终点的。

如果 `i + nums[i] >= nums.size()-1` 则说明这个 `i` 可以一步到位 直接赋值为 `1`

如果 `nums[i+1] == nums[i] - 1` 的时候 ，例如 `3 ,2 ,1 ，1 ，1` 可以说我们

`dp[i] = dp[i+1]`

否则采取 贪心的做法去找寻 最小的一个.

### **ac_code**
```c
class Solution {
public:
    int jump(vector<int>& nums) {
        vector<int> dp(nums.size(),0);
        for(int i = nums.size()-2;i>=0;--i){
            if(nums[i]==0) continue;
            if(nums[i] + i>=nums.size()-1){
                dp[i] = 1;
            }
            else if(nums[i+1] == nums[i] - 1){
                    dp[i] = dp[i+1];
                }
            else{
                int min_val = INT_MAX;
                for(int j = i+nums[i]; j>i;--j){
                    if(dp[j]<min_val&&dp[j]) min_val = dp[j];
                }
                dp[i] =( min_val == INT_MAX )? 0 :min_val + 1;
            }
        }
       return dp[0];
    }
};
```