[TOC]

# 向前星

```python
class edge:
    def __init__(self):
        self.nex = 0
        self.t = 0
        self.w = 0

# 下标从1开始
E = [edge()]
H = {}

def add_path(f, t, w):  # 在前向星中加边
    global E, H
    e = edge()
    e.nex = H.get(f, 0)
    e.t = t
    e.w = w
    E.append(e)
    H[f] = len(E) - 1

def nextedgeid(f):  # 生成器，可以用在for循环里
    global E, H
    i = H.get(f,0)
    while i:
        yield i
        i = E[i].nex

# travel graph

# 添加边
G = [[1,2,0], [2,3,4],[3,4,5], [4,21,1]]
for e in G:
    add_path(e[0], e[1], e[2])

# 遍历
for i in nextedgeid(f):
    print("{}: {}".format(E[i].t, E[i].w))
```

# 图的存储

对于一个图 $n_{edge}  $ $n_{node}$, 如果 $n_{node} << n_{edge}$ 那么我们可以使用邻接矩阵来存储图

反之 $n_{node} >> n_{edge}$ 那么我们就需要选择 向前星 或者 邻接矩阵来存储图



# 最短路径算法



## 多源最短路径

```python
# version 1 
# 只计算距离
def floyd(G):
  for k in range(n): # 中间的节点 k 一定是最外层循环
    for i in rang(n):
      for j in range(n):
        if i != j :
					dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
          
# version 2 
# 回归路径
path = [[0  for i in range(n)] for j in range(n)]
def recover_path(path, f, t):
  # print(f, t)
  if path[f][t] == 0:
    return []
  if f == t:
    return []
  left = recover_path(path,f, path[f][t])
  right = recover_path(path,path[f][t] , t)
  return left + [path[f][t]] + right

def floyd(G):
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if i != j and G[i][j] > G[i][k]+G[k][j]:
          G[i][j] = G[i][k]+G[k][j]
          path[i][j] = k
```



## 单源最短路径



```python
```



# 拓扑排序

```python
# 维护一个出边的计数
outs = [len(tos) for tos in graph]
# 维护一个逆边
froms = [[] for i in range(n)]
for i, tos in enumerate(graph):
  for to in tos:
    froms[to].append(i)
# 使用队列维护出边为 0 的 节点.
q = collections.deque([])
for i in range(len(outs)):
  if outs[i] == 0:
    q.append(i)
res = []
while len(q):
  c = q.popleft()
  res.append(c)
  for f in froms[c]:
    outs[f] -= 1
    if outs[f] == 0: # 当前节点沦为 没有出边的节点
      q.append(f)
print(res)
```



