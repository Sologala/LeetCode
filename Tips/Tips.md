记录一些编程中进行判断的高效的小Tips

1. 判断是否是2的`power` 	

   1. ```c++
      num & (num -1) == 1 //代表不是2的幂
      ```

##  计算汉明距离（统计1 的个数）

```c++
 int hammingWeight(uint32_t n) {
        int cnt = 0 ;
        while (n){
            cnt++;
            n &=  (n - 1);
        }
        return cnt;
    }
```





# 数组循环右移动

```
void loopR(int a[],int l,int r,int k){
    //reverse all
    reverse(a,l,r);
    //reverse k-th
    reverse(a,l,l+k-1);
    //reverse tail
    reverse(a,l+k,r);
}
```



