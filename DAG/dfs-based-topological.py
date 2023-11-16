# 基于深度优先搜索的拓扑排序DAG
from collections import defaultdict


def topological_sort(graph):
    visited = set()
    result = []

    def dfs(node):
        nonlocal visited, result
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        result.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return result[::-1]


# 使用defaultdict创建有向图
graph = defaultdict(list)
graph['a'] = ['b', 'c']
graph['b'] = ['d']
graph['c'] = ['d']
graph['d'] = ['e']
graph['e'] = []

topological_order = topological_sort(graph)
print("Topological Order:", topological_order)


# Topological拓扑学
# 拓扑学（Topology）是数学的一个分支，研究空间的性质在连续映射下的不变性。具体来说，拓扑学关注的是空间中的点、集合、映射之间的一些基本性质，而这些性质在连续映射下保持不变。拓扑学不关心具体的度量和距离，而是关注形状和空间结构的抽象特征。
