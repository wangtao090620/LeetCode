## 初始化操作

### 初始化数组

```
 dp, stack = [0] * (len(s) + 1), []

```

### 初始化二维数组

```
dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

例如：

t = [[0 for _ in range(2)] for _ in range(3)]

[[0, 0], [0, 0], [0, 0]]


```

### 偏移数组

```
       (x-1,y)
(x,y-1) (x,y) (x,y+1)
       (x+1,y)

directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

```