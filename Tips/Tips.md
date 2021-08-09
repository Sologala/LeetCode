记录一些编程中进行判断的高效的小Tips

## 判断是否是2的`power` 	

1. 
   
   ```c++
   num & (num -1) == 1 //代表不是2的幂
   ```

# lowbit

返回参数转为二进制后,**最后一个1的位置**所代表的数值。

```c++
int lowbit(int x){
  return x & (-x);
}
n = 12
bin(n),bin(lowbit(n))
('0b1100', '0b100')
```

例如 `12`,则返回最后一个1 代表的` 4`

##  计算汉明距离（统计1 的个数）

```c++
def hammingWeight(x):
    cnt = 0
    while x:
        cnt += 1
        x &= (x - 1)
    return cnt
n = 31728648
bin(n), hammingWeight(n)
          
('0b1111001000010010000001000', 8)
```

同时可以在统计的时候，输出某一位

```python
def hammingWeight(x):
    cnt = 0
    while x:
        cnt += 1
        print(bin(x), bin(x ^ (x & (x - 1))))
        x &= (x - 1)
    return cnt
n = 231
bin(n), hammingWeight(n)
0b11100111 0b1
0b11100110 0b10
0b11100100 0b100
0b11100000 0b100000
0b11000000 0b1000000
0b10000000 0b10000000
```

第二列代表了最低位的数据`x ^ (x & (x - 1))`

同样也可以利用`lowbit`

```python
t = 13
while t > 0:
    lb = lowbit(t & (-t))
    print(bin(lb), bin(t))
    t -= lb
0b1 0b1101
0b100 0b1100
0b1000 0b1000
```



# 数组循环右移动

```c++
void loopR(int a[],int l,int r,int k){
    //reverse all
    reverse(a,l,r);
    //reverse k-th
    reverse(a,l,l+k-1);
    //reverse tail
    reverse(a,l+k,r);
}
```



