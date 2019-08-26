![face.jpg](https://pic.leetcode-cn.com/5f44c38cfca16ba4f3886e1c9e298c5ab18a215dc25e965ec357a430e783b3af-face.jpg)

/*
[@Github _ Sologala](https://github.com/Sologala/LeetCode.git)

[`1015`]**可被 K 整除的最小整数**|**smallest-integer-divisible-by-k**

*/

给定正整数 K，你需要找出可以被 K 整除的、仅包含数字 1 的最小正整数 N。

返回 N 的长度。如果不存在这样的 N，就返回 -1。

 

示例 1：

输入：1
输出：1
解释：最小的答案是 N = 1，其长度为 1。
示例 2：

输入：2
输出：-1
解释：不存在可被 2 整除的正整数 N 。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-integer-divisible-by-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## **Solution** 



对于任何一个整数我们都可以把这个整数表示称为`n = a * K + b`  ，当这个数字对于我们的K取余操作的时候，我们可以发现如下
$$
n \% K = (a * K + b) \% K  = b
$$
因此我们可以先让这个数字每次都`n %= K ` 这样的话就不会出现这个数字越界

**ac_code**

```c
class Solution {
public:
    int smallestRepunitDivByK(int K) {
        int len = 1 ;
        if(K%2==0||K%5 == 0) return -1;
        int t = 1;
        while(t%K!=0){
            t%=K;
            t = t*10 + 1;
            len++;
        }
        return len;
    }
};
```