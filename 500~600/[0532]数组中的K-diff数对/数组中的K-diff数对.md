![face.jpg](https://pic.leetcode-cn.com/5f44c38cfca16ba4f3886e1c9e298c5ab18a215dc25e965ec357a430e783b3af-face.jpg)

/*
    Sologala   @github    https://github.com/Sologala/LeetCode.git

   [532]数组中的K-diff数对
     |     k-diff-pairs-in-an-array

*/

给定一个整数数组和一个整数 k, 你需要在数组里找到不同的 k-diff 数对。这里将 k-diff 数对定义为一个整数对 (i, j), 其中 i 和 j 都是数组中的数字，且两数之差的绝对值是 k.

示例 1:

输入: [3, 1, 4, 1, 5], k = 2
输出: 2
解释: 数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
尽管数组中有两个1，但我们只应返回不同的数对的数量。
示例 2:

输入:[1, 2, 3, 4, 5], k = 1
输出: 4
解释: 数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5)。
示例 3:

输入: [1, 3, 1, 5, 4], k = 0
输出: 1
解释: 数组中只有一个 0-diff 数对，(1, 1)。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/k-diff-pairs-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## **Solution** 

要找是否出现配对的数字,我们可以使用`hash` 来存储已经便利过的数组,看是否有出现过配对的 `n-k` 或者 `n+k`.

这里为了避免情况复杂,我们认为当 `k<0` 的情况视为不正确的,直接返回`0`

这里为了避免再一次循环中比较两次,因此事先我们先对整个数组排序,这样我们只需要去判断 `n-k` 了.

我们再建立一种`Key` 来保存一个数据表示`(a,b)` 然后建立这种`Key` 的`hash` 来判断是否出现过了这个数据.

如果没有出现,就`cnt++`

### **ac_code**
```c
class Key{
public:
    int a,b;
    Key(int _a, long _b) :  a(_a), b(_b) {}
};

struct KeyHash{   //自定义Hash函数
    size_t operator()(const Key& k) const{
        return std::hash<int>()(k.b)^(std::hash<int>()(k.a)+1);
    }
};

struct KeyEqual{  //自定义操作符号
    bool operator()(const Key& x, const Key& y) const{
        return x.a == y.a && x.b == y.b;
    }
};
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        unordered_map<int,int> m;
        if(k<0) return 0;
        sort(nums.begin(),nums.end());
        unordered_map<Key,int,KeyHash,KeyEqual> res;
        int ret = 0;
        for(auto n : nums){
            Key p(n-k,n);
            if(m[n-k]&&res.count(p) == 0)
                res[p]++,ret++;
            m[n]++;
        }
        return ret;
    }
};
```