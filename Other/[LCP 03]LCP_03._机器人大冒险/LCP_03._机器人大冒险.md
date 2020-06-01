![face.jpg](https://pic.leetcode-cn.com/5f44c38cfca16ba4f3886e1c9e298c5ab18a215dc25e965ec357a430e783b3af-face.jpg)

/*
[@Github _ Sologala](https://github.com/Sologala/LeetCode.git)

[`LCP 03`]**LCP_03._机器人大冒险**|**LCP_03._Programmable_Robot**

*/

力扣团队买了一个可编程机器人，机器人初始位置在原点(0, 0)。小伙伴事先给机器人输入一串指令command，机器人就会无限循环这条指令的步骤进行移动。指令有两种：

```
U: 向y轴正方向移动一格
R: 向x轴正方向移动一格。
```


不幸的是，在 xy 平面上还有一些障碍物，他们的坐标用obstacles表示。机器人一旦碰到障碍物就会被损毁。

给定终点坐标(x, y)，返回机器人能否完好地到达终点。如果能，返回true；否则返回false。



## **Solution** 

![image-20200601220927386](https://tva1.sinaimg.cn/large/007S8ZIlly1gfd56tqyecj31a00m6mzb.jpg)

可以发现坐标存在一定的规律。那么只需要枚举一遍给定的指令字符串，以$(0,0)$ 为起点生成 $[(0,0),(0,1),(1,1),(2,1)]$，并且观察到，经过一个循环实际上，坐标是$(x + x_{off}, y + y_{off})$。

设target的坐标为$(x,y)$，例如出现在图中绿黄色部分，需要判断之前经过了$temp$个循环。$temp = min(x // x_{off}, y // y_{off})$. 然后将target坐标对齐到$(0,0)$ 坐标系。

## 判断是否能够到达target

只需要判断是否出现在$[(0,0),(0,1),(1,1),(2,1)]$即可。



那么本问题只需要判断是否可达终点，随后在以此判断是否会碰上obstacles就可以了。

这里要注意排除在终点右上方的obstacles。



### **ac_code**

```python
class Solution:
    def judge(self, targ, s, x_off, y_off):
        x, y= targ
        temp = min(x // x_off , y // y_off)
        x ,y = x - x_off * temp , y - y_off * temp
        return (x, y) in s 
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        # simulate all points in round 1
        s = [(0, 0)]
        x_off, y_off = 0, 0
        for c in command:
            if c == 'U':
                s.append((s[-1][0], s[-1][1] + 1))
                y_off += 1
            else:
                s.append((s[-1][0] + 1, s[-1][1]))
                x_off += 1

        obstacles.sort(key = cmp_to_key(lambda x, y: x[0] < y[0] if x[0] != y[0] else x[1] < y[1]))
        # judge weather it can get end point
        
        if self.judge((x,y), s, x_off, y_off) == False:
            return False
        for obs in obstacles:
            if obs[0] >= x and obs[1] >= y:
                continue  
            if self.judge((obs[0],obs[1]), s, x_off, y_off):
                return False
        return True

```