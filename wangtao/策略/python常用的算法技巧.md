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

## 链表

```
leetCode 142、148、234、0287

fast = slow = head
# 快指正到尾部，慢指针正好在链表一半的位置
while fast and fast.next:
    fast = fast.next.next
    slow = slow.next


这个技巧适用于链表是否是回文链表，给定一个链表，返回链表开始入环的第一个节点



```