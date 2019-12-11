## 初始化操作

### 初始化数组

```
 dp, stack = [0] * (len(s) + 1), []

```

### 初始化二维数组

```
dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

```