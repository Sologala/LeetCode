![](https://github.com/Sologala/SomeThings/blob/master/face.jpg?raw=true)

/*
    Sologala   @github    https://github.com/Sologala/LeetCode.git

   [957]N 天后的牢房
     |     prison-cells-after-n-days

*/

8 间牢房排成一排，每间牢房不是有人住就是空着。

每天，无论牢房是被占用或空置，都会根据以下规则进行更改：

如果一间牢房的两个相邻的房间都被占用或都是空的，那么该牢房就会被占用。
否则，它就会被空置。
（请注意，由于监狱中的牢房排成一行，所以行中的第一个和最后一个房间无法有两个相邻的房间。）

我们用以下方式描述监狱的当前状态：如果第 i 间牢房被占用，则 cell[i]==1，否则 cell[i]==0。

根据监狱的初始状态，在 N 天后返回监狱的状况（和上述 N 种变化）。

 

示例 1：

输入：cells = [0,1,0,1,1,0,0,1], N = 7
输出：[0,0,1,1,0,0,0,0]
解释：
下表概述了监狱每天的状况：
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

示例 2：

输入：cells = [1,0,0,1,0,0,1,0], N = 1000000000
输出：[0,0,1,1,1,1,1,0]



## **Solution** 

这道题 是看了答案写的，`%14` 自己试出来了 ，但是发现当`%14 == 0`之后 与答案不对 ，困扰了我很久，后来看到当`0`次的时候实际上是需要循环`14`次的。

并且要注意 一旦 循环就要把默认的`cells[0] cells[1]` 都设置为 `0` 因为这两个位置的数字都没有左右。

### **ac_code**
```c
class Solution {
public:
    vector<int> prisonAfterNDays(vector<int>& cells, int N) {
        int len = cells.size();
        N %= 14 ;
        N = (N==0 ? 14 : N); 
        vector<int> ret(len,0);
        vector<int>*  r[2] = {};
        r[0] = &cells;
        r[1] = &ret;
        int i = 0;
        for(    ;i<N;++i){
            for(int j =1;j<len-1;++j){
                r[(i+1)%2]->at(j) =(r[i%2]->at(j-1) == r[i%2]->at(j+1)? 1 : 0);
            }
            if(i==0){
                r[i]->at(0) = 0;
                r[i]->at(r[i]->size()-1) = 0;
            }
        }
        return *(r[i%2]);
    }
};
```