### 常用的模板

```
visited = set()

def dfs(node, visited):
    visited.add(node)

    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)

```