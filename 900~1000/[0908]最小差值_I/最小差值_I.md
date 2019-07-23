![face.jpg](https://pic.leetcode-cn.com/5f44c38cfca16ba4f3886e1c9e298c5ab18a215dc25e965ec357a430e783b3af-face.jpg)

/*
    Sologala   @github    https://github.com/Sologala/LeetCode.git

   [908]最小差值 I
     |     smallest-range-i

*/

给定一个整数数组 A，对于每个整数 A[i]，我们可以选择任意 x 满足 -K <= x <= K，并将 x 加到 A[i] 中。

在此过程之后，我们得到一些数组 B。

返回 B 的最大值和 B 的最小值之间可能存在的最小差值。

 

示例 1：

输入：A = [1], K = 0
输出：0
解释：B = [1]
示例 2：

输入：A = [0,10], K = 2
输出：6
解释：B = [2,8]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-range-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## **Solution** 

要找到发生改变之后的最大值与最小值的差,而这个最大值与最小值必定是当前状态下的最大值最小值发生改变得到的.可以理解成为变换之后的**短板**.

我们找到当前状态的最小值与最大值 然后让最小值 `+K`  最大值 `-K`  然后在比较两个值的差,如果差 `<0` 那么证明可以取其中某个值使得所有的数字都调整为那个数字,从而差值为 `0`.



### **ac_code**
```c
class Solution {
public:
    int smallestRangeI(vector<int>& A, int K) {
        if(A.size() == 0) return 0;
        int maxn = INT_MIN,minn = INT_MAX;
        for(int n : A){
            maxn = max(maxn , n);
            minn = min(minn , n);
        }
        maxn -= K;
        minn += K;
        return (maxn - minn < 0 ? 0 : maxn - minn); 
    }
};
```