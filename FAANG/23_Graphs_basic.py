# 重新看待这个数据结构
# 复杂多变，链表是有方向的，2D矩阵也是可以随意遍历的每个节点有自己的值，而图则复杂的多，包括这些方面：
# 1. 有无方向上，分undirected和directed
# -  directed又有单向和双向之分
# 2. 权重有无上，可能是有权图，也可以是无权图
# 3. 甚至有连接和非连接的图，图中的节点不一定都是相连的
# Graph是LinkedList，Tree，2dArray的一个总集

# Constraints:
# Cycic? Unconnected? Weighted? Directed?

# 使用AdjList进行表达是一个常用方法
from collections import deque

adjList = {
    0: [1, 3],
    1: [0],
    2: [3, 8],
    3: [0, 4, 5, 2],
    4: [3, 6],
    5: [3],
    6: [4, 7],
    7: [6],
    8: [2],
}


def bfsTraversal(adjList):
    result = []
    queue = deque()
    visited = set()

    queue.append(0)
    while queue:
        node = queue.popleft()
        result.append(node)
        visited.add(node)

        for neighber in adjList[node]:
            if neighber in visited:
                continue
            queue.append(neighber)

    return result


print(bfsTraversal(adjList))


def dfs(adjList, node, result, visited):
    if node in visited:
        return

    result.append(node)
    visited.add(node)

    for neighber in adjList[node]:
        dfs(adjList, neighber, result, visited)


def dfsTraversal(adjList):
    result = []
    visited = set()

    dfs(adjList, 0, result, visited)
    return result


print(dfsTraversal(adjList))
