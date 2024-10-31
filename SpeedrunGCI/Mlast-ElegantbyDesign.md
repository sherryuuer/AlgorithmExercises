## Bitwise Manipulation
- AND, OR, XOR
- left shift, right shift
- Binary representation：power of 2->2^0~
- Efficient sorting
- **!!想清楚再写！不要一道简单题各种小错误完蛋**
**Flipping an Image**
```python
# calculate the half length/may be I want use left and right pointer
# loop the half of the num
# calculate the xor with 1 and swap it with the right half num
# return the image
def flip_and_invert_image(image): # n * n
    n = len(image)
    for row in range(n):
        curRow = image[row]
        left, right = 0, n - 1
        while left <= right: # time O(n^2) space O(1)
            curRow[left] ^= 1
            if left != right:
                curRow[right] ^= 1
            curRow[left], curRow[right] = curRow[right], curRow[left]
            left += 1
            right -= 1
    return image
```

## Sliding Window
- Contiguous data
- Processing subsets of elements
- Efficient computation time complexity

**Sliding Window Maximum**
```python
from collections import deque
# [1,2,3,4,5,6,7,8,9,10]
# 固定窗口
# 最佳方案可能对我有点难，也许我用heapq是最容易实现的
# 最佳方案，q中存储的是index，q最多可以存储w个值！并且是按照值从大到小的顺序，很精妙
def find_max_sliding_window(nums, w):
    result = []
    queue = deque() # space O(w)
    left, right = 0, 0

    while right < len(nums): # time O(n)
        # mantainance the queue as a desc queue
        while queue and nums[queue[-1]] < nums[right]:
            queue.pop()
        queue.append(right)

        # mantainance the boundary
        if queue[0] < left:
            queue.popleft()

        # detect size w and get the maximum num
        if (right + 1) >= w:
            result.append(nums[queue[0]])
            left += 1

        right += 1

    return result
```

## Union Find
1. Property-based grouping
2. Set combination
3. Graph data organization

**Number of Islands**
```python
# 已有的代码部分
class UnionFind:

    # Initializing the parent list and count variable by traversing the grid
    def __init__(self, grid):
        self.parent = []
        self.rank = []
        self.count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent.append(i * n + j) # [0, 1, 2, 3...]
                    self.count += 1
                else:
                    self.parent.append(-1)
                self.rank.append(0)

    # Function to find the root parent of a node
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    # Function to connect components
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1

    # Function to return the number of conencted components consisting of "1"s
    def get_count(self):
        return self.count

from union_find import UnionFind

def num_islands(grid): # clever!
    if not grid:
        return 0
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    uf = UnionFind(grid)
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                for dr, dc in directions:
                    r, c = i + dr, j + dc
                    if r < 0 or r >= m or c < 0 or c >= n:
                        continue
                    if grid[r][c] == "1":
                        uf.union(i * n + j, r * n + c)

    return uf.count
```
