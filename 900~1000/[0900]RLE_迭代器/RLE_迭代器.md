![face.jpg](https://pic.leetcode-cn.com/5f44c38cfca16ba4f3886e1c9e298c5ab18a215dc25e965ec357a430e783b3af-face.jpg)

/*
    Sologala   @github    https://github.com/Sologala/LeetCode.git

   [900]RLE 迭代器
     |     rle-iterator

*/

编写一个遍历游程编码序列的迭代器。

迭代器由 RLEIterator(int[] A) 初始化，其中 A 是某个序列的游程编码。更具体地，对于所有偶数 i，A[i] 告诉我们在序列中重复非负整数值 A[i + 1] 的次数。

迭代器支持一个函数：next(int n)，它耗尽接下来的  n 个元素（n >= 1）并返回以这种方式耗去的最后一个元素。如果没有剩余的元素可供耗尽，则  next 返回 -1 。

例如，我们以 A = [3,8,0,9,2,5] 开始，这是序列 [8,8,8,5,5] 的游程编码。这是因为该序列可以读作 “三个八，零个九，两个五”。

 

示例：

输入：["RLEIterator","next","next","next","next"], [[[3,8,0,9,2,5]],[2],[1],[1],[2]]
输出：[null,8,8,5,-1]
解释：
RLEIterator 由 RLEIterator([3,8,0,9,2,5]) 初始化。
这映射到序列 [8,8,8,5,5]。
然后调用 RLEIterator.next 4次。

.next(2) 耗去序列的 2 个项，返回 8。现在剩下的序列是 [8, 5, 5]。

.next(1) 耗去序列的 1 个项，返回 8。现在剩下的序列是 [5, 5]。

.next(1) 耗去序列的 1 个项，返回 5。现在剩下的序列是 [5]。

.next(2) 耗去序列的 2 个项，返回 -1。 这是由于第一个被耗去的项是 5，
但第二个项并不存在。由于最后一个要耗去的项不存在，我们返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rle-iterator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## **Solution** 

​	首先这个数组我们需要保存下来,然后设置一个下标`cur` 来表示当前我们正在处理那个数,如果当前参数`n>A[i]` 那么我们要全部扣除当前这个 并且 `cur+=2`移动到下一个数字.这个过程使用循环来做,知道全部扣完,但是要处理`cur+1>=A.size()` 的情况需要 `return -1` 	 

这里要注意的石 **我们要返回的是上一个处理过的数** 也就是说 如果循环扣除之后发现 `n==0` 就不能返回当前这个,而是需要返回上一次那个数.



### **ac_code**
```c
class RLEIterator {
public:
    vector<int> Arr;//开一个新的数组来保存.
    int cur;
    RLEIterator(vector<int>& A) {
        Arr = A;
        cur = 0;
    }
    int next(int n) {
        int ret;
        while(n&&cur+1<Arr.size()&&n>=Arr[cur]){
            if(Arr[cur]!=0){//0个的略过
                n-=Arr[cur];
                ret = Arr[cur+1];
            }
            cur+=2;
        }
        if(cur+1>=Arr.size()) //没有了 
            return -1;
        if(n==0) return ret;//刚刚好处理完 输出上一个
        Arr[cur] -= n;
        return Arr[cur+1];
    }
};

```