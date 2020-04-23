![face.jpg](https://pic.leetcode-cn.com/5f44c38cfca16ba4f3886e1c9e298c5ab18a215dc25e965ec357a430e783b3af-face.jpg)

/*
[@Github _ Sologala](https://github.com/Sologala/LeetCode.git)

[`154`]**寻找旋转排序数组中的最小值 II**|**find-minimum-in-rotated-sorted-array-ii**

*/



## **Solution** 

1. O(n)遍历找断崖。

2. 二分法O(log~2~N)

    对于一个列表，分为左右两个单增的序列。如下：

    [1,1,2,3,**0**,**1**,**1**]

    由于最小值一定出现在右边序列，我们可以假设 `nums[j]`为当前已知的最优。

    计算中点m,如果 `nums[m] > nums[j]`那么一定出现在左半部分，从 `nums[0~i]` 都不会是解。 将 ` i = m + 1 `

    如果 `nums[m] < nums[j]` ，出现了新的更优解，`j = m`

    除了上面两种情况之外，则出现 `nums[m] == nums[i | j]`。这个时候再将 `j--`；

### **ac_code**
```c
class Solution {
public:
    int findMin(vector<int>& nums) {
        if(nums[0] < nums[nums.size()- 1]) return nums[0];
        int i = 0 ,j = nums.size()-1;
        while(i<j){
            if(i + 1 == j) return min(nums[i], nums[j]);
            int m = (i + j) / 2;
            if(nums[m] > nums[j]) i = m + 1;
            else if(nums[m] < nums[j]) j = m;
            else j--;
        }
        return nums[i];
    }
};
```