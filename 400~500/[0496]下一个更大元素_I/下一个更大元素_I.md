![](https://github.com/Sologala/SomeThings/blob/master/face.jpg?raw=true)

/*
    Sologala   @github    https://github.com/Sologala/LeetCode.git

   [496]下一个更大元素 I
     |     next-greater-element-i

*/

给定两个**没有重复元素**的数组 `nums1` 和 `nums2` ，其中`nums1` 是 `nums2` 的子集。找到 `nums1` 中每个元素在 `nums2` 中的下一个比其大的值。

`nums1` 中数字 **x** 的下一个更大元素是指 **x** 在 `nums2` 中对应位置的右边的第一个比 **x** 大的元素。如果不存在，对应位置输出-1。

**示例 1:**

```
输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
    对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
    对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
```

**示例 2:**

```
输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]
解释:
    对于num1中的数字2，第二个数组中的下一个较大数字是3。
    对于num1中的数字4，第二个数组中没有下一个更大的数字，因此输出 -1。
```

##**Solution** 

先处理`nums2` 数组，统计每个数字 他的最后一个数字是多少 。

我们可以使用一个 单调栈来做，栈中记录的是下标。

策略为：

栈空入栈，如果当前元素比 栈顶元素的位置的数字大，一直出栈 并且记录当前数字的 下一个大的数字是 当前元素。

最后将 当前的下标入栈。

最后我们讲`nums1` 的数据 都翻译一下就好了。

### **ac_code**
```c
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        int max_val = -1;
        int s[1000],top =-1;
        unordered_map<int,int> m;
        for(int i = 0;i<nums2.size();++i){
            if(top==-1){
                s[++top] = i;
                continue;
            }
            while(top!=-1&&nums2[i] > nums2[s[top]]){
                m[nums2[s[top--]]] = nums2[i];
            }
            s[++top] = i;
        }
        for(int i = 0;i<nums1.size();++i){
            nums1[i] = m.count(nums1[i]) == 0 ? -1 : m[nums1[i]]; 
        }
        return nums1;
    }
};
```