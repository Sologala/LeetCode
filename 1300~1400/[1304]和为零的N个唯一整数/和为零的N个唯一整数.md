![face.jpg](https://pic.leetcode-cn.com/5f44c38cfca16ba4f3886e1c9e298c5ab18a215dc25e965ec357a430e783b3af-face.jpg)

/*
[@Github _ Sologala](https://github.com/Sologala/LeetCode.git)

[`1304`]**和为零的N个唯一整数**|**Find_N_Unique_Integers_Sum_up_to_Zero**

*/



## **Solution** 

生成 `n/2`个随机数,另外一半弄成负数。

### **ac_code**
```c
class Solution {
public:
    unordered_map<int,int> m;
    int getRanNum(){
        srand(time(0));
        int num = rand()%1000;
        while(m.count(num))
            num = rand()%1000;
        m[num] = 1;
        return num;
    }
    vector<int> sumZero(int n) {
        vector<int> res(n,0);
        int i;
        for(i = 0 ;i < n/2 ;++i)
            res[i] = getRanNum();
        if( n%2 == 1) i++;
        for(    ; i< n;++i)
            res[i] = - res[n - i - 1];
        //cout<<accumulate(res.begin() ,res.end(),0);
        return res;
    }
};
```