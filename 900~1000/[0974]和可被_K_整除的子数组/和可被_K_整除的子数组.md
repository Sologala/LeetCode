![face.jpg](https://pic.leetcode-cn.com/5f44c38cfca16ba4f3886e1c9e298c5ab18a215dc25e965ec357a430e783b3af-face.jpg)

/*
[@Github _ Sologala](https://github.com/Sologala/LeetCode.git)

[`974`]**和可被 K 整除的子数组**|**subarray-sums-divisible-by-k**

*/

给定一个整数数组 `A`，返回其中元素之和可被 `K` 整除的（连续、非空）子数组的数目。

> 示例：
>
> 输入：A = [4,5,0,-2,-3,1], K = 5
> 输出：7
> 解释：
> 有 7 个子数组满足其元素之和可被 K = 5 整除：
> [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]




## **Solution** 

使用前缀和，并且记录每次前缀和的余数的次数。

## 同余定理

如果$p[i] = \sum_{0}^{i} a[i]$为前缀和，若满足某子数组的和为$\%K == 0$，那么比满足
$$
(p[j]-p[i]) \%K == 0\\
p[j] \% K == p[i] \%K
$$


### **ac_code**
```c
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        s = 0
        cnt = {0:1}
        res = 0
        for n in A:
            s += n
            remain = s % K
            if remain in cnt.keys():
                res += cnt[remain]
                cnt[remain] += 1
            else:
                cnt[remain] = 1
        return res
```