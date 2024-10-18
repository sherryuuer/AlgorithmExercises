# (u, v, w) with a start node k, calculate the time it will take to get all nodes
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2

times = [[1, 2, 9], [1, 4, 2], [2, 5, 1], [4, 2, 4],
         [4, 5, 6], [3, 2, 3], [5, 3, 7], [3, 1, 5]]
n = 5
k = 1
# 14


# adjList: {u: (v, w)}
# heapq [length, node]
# visited: set()
# shortest = {node: length}
def networkTimeDelay(n, k, times):
    import heapq
    adjList = {}

    for i in range(1, n + 1):
        adjList[i] = []

    for u, v, w in times:
        adjList[u].append([v, w])  # O(E)

    minHeap = [[0, k]]
    shortest = {}  # O(n)

    while minHeap:
        w1, v1 = heapq.heappop(minHeap)  # O(nlogn) as E > n so O(Elogn)
        if v1 in shortest:
            continue
        shortest[v1] = w1

        for v2, w2 in adjList[v1]:
            if v2 not in shortest:
                heapq.heappush(minHeap, [w1 + w2, v2])  # O(Elogn)

    if len(shortest) == n:
        return max(shortest.values())

    return -1


print(networkTimeDelay(n, k, times))
# Space：O(E + N)
# Dijkstra算法不回头，是贪婪的，这是因为权重没有负数，不然的话就会失效了
# Bellman算法可以有负数，它使用了动态规划的思想


def networkDelayTime(times, N, K):
    # Step 1: Initialize distances array
    dist = [float('inf')] * (N + 1)
    dist[K] = 0  # Starting point has distance 0

    # Step 2: Relax edges up to N-1 times
    for i in range(N - 1):
        updated = False  # Track if any update occurs in this iteration
        for u, v, w in times:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True  # Mark that an update occurred

        if not updated:  # If no update, break early
            break

    # Step 3: Get the maximum distance to determine the delay to all nodes
    max_dist = max(dist[1:])

    # If there's a node that we can't reach, return -1
    return max_dist if max_dist != float('inf') else -1


# Example usage:
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
N = 4
K = 2
print(networkDelayTime(times, N, K))  # Output: 2
