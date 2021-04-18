RMQ问题(**Range Minimum/Maximum Query**) 。

 给定一个 数组， 查询 $range(l, r)$ 中的最大值.

1. **Plain algo** : 使用 `for (int i = l; i<= r; i++)` 遍历查找最大值。当数据量大之后，速度十分慢。

2. 解决**RMQ**问题的主要办法分为`off-line` 以及 `on-line`的办法。

3. `off-line`可以预先使用二维dp数组维护区间。

	使用$dp[i][j]$ 表示 第i 位开始连续$2^j$个数字中的最值

	$dp[i][j] = min(dp [i][j - 1], dp [i + \frac{j - 1}{2})][j - 1])$

	意思就是从$i$ 开始的连续区间内，利用二分的思想来维护一个最值。

	![img](RMQ问题(Range MinimumMaximum Query) .assets/1460000023293056)

	###### 初始化

	```c++
	void rmq_init(vector<int> &data)
	{
	    int maxJ = ceil(log(N) / log(2));
	
	    vector<vector<int>> dp(N, vector<int>(maxJ + 1, 0));
	
	    for (int i = 0; i < N; ++i)
	        dp[i][0] = v[i];
	    for (int j = 1; j < maxJ; ++j)
	        for (int i = 0; i + (1 << (j - 1)) < N; ++i)
	            dp[i][j] = max(dp[i][j - 1], dp[i + (1 << (j - 1))][j - 1]);
	}
	```

	

	###### 查询

	![img](RMQ问题(Range MinimumMaximum Query) .assets/1460000023293057)

	```c++
	int find(vector<vector<int>> &dp, int l, int r)
	{
	    int k = log(r - l + 1) / log(2);
	    return max(dp[l][k], dp[r - (1 << k)][k]);
	    //这里的区间有些许与图示不一样，r - (1 << k) ，但是无关紧要，且只是有一个重复的值而已。
	}
	```

	