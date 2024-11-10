## Bitwise Manipulation
- AND, OR, XOR
- left shift, right shift
- Binary representation：power of 2->2^0~
- Efficient sorting
- **!!想清楚再写！不要一道简单题各种小错误完蛋**
### **Flipping an Image**
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

### **Sliding Window Maximum**
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

### **Longest Repeating Character Replacement**

- test case: [a, a, b, b, c, c, b] k = 2 return 5

- hashmap(char: count) to track the freq of chars
- left, right = 0, 0 and create sliding windows
- max_length = 0

- sliding window will get the most freq char and if len(r - l + 1) - freq > k move the window
- update the max_length


```python
from collections import defaultdict


def longest_repeating_character_replacement(s, k):
    if not s: return 0
    if k >= len(s): return len(s)

    max_length = 0
    hashmap = defaultdict(int) # char: count in window
    left = 0

    for right in range(len(s)): # time O(n) space O(1)
        hashmap[s[right]] += 1
        # get the most freq char from hashmap
        char = max(hashmap, key=hashmap.get)

        # calculate the window size check if vaild
        cur_length = right - left + 1
        if cur_length - hashmap[char] <= k:
            max_length = max(cur_length, max_length)
        # else: left += 1 -> update the hashmap
        else:
            hashmap[s[left]] -= 1
            left += 1

    return max_length


# manual test [a, a, b, b, c, c, b]
# k = 2
# max_length = 5
# hashmap = {a:0, b:2, c:2}
# left, right = 2, 6
```

### **Longest Substring without Repeating Characters**

```python
def find_longest_substring(input_str):
    if not input_str:
        return 0

    max_length = 0
    left = 0
    hashmap = {} # O(n)

    for right in range(len(input_str)): # time O(n)
        char = input_str[right]
        if char in hashmap and hashmap[char] >= left:
            left = hashmap[char] + 1

        hashmap[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length
```

### **Best Time to Buy and Sell Stock**

```python
def max_profit(prices):
    if not prices:
        return 0

    max_profit = 0

    left = 0 # space O(1)
    for right in range(len(prices)): # time O(n)
        p = prices[right]
        if p > prices[left]:
            max_profit = max(max_profit, p - prices[left])
        else:
            left = right
    return max_profit

# [7, 1, 5, 3, 6, 4, 5]
# max = 5
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

### **Longest Consecutive Sequence**

```python
def longest_consecutive_sequence(nums):
    hashset = set(nums)
    max_length = 0

    for n in nums:
        if n - 1 not in hashset:
            cur_num = n
            cur_length = 1

            while cur_num + 1 in hashset:
                cur_num += 1
                cur_length += 1

            max_length = max(max_length, cur_length)

    return max_length
```
- 成为连续序列的元素不需要是连续的，时间和空间复杂度都是O(n)
- 这里还是选择使用hashset方法，代码实现难度较低

```python
class UnionFind:
    def __init__(self, nums):
        self.parent = { n: n for n in nums }
        self.size = { n: 1 for n in nums }
        self.max_length = 1

    def find(self, num):
        while num != self.parent[num]:
            self.parent[num] = self.find(self.parent[num])
        return self.parent[num]

    def union(self, num1, num2):
        root1 = self.find(num1)
        root2 = self.find(num2)

        if root1 != root2:
            if self.size(root1) < self.size(root2):
                self.parent(root1) = root2
                self.size(root2) += self.size(root1)
                self.max_length = max(self.max_length, self.size(root2))
            else:
                self.parent(root2) = root1
                self.size(root1) += self.size(root2)
                self.max_length = max(self.max_length, self.size(root1))

def longest_consecutive_sequence(nums):
    if len(nums) == 0:
        return 0

    uf = UnionFind(nums)

    for n in nums:
        if n + 1 in uf.parent:
            uf.union(n, n + 1)

    return uf.max_length
```

### **Last Day Where You Can Still Cross**
- 第一直觉是BFS找路

```python
from collections import deque


def bfs(days, rows, cols, cells):
    grid = [[0] * cols for _ in range(rows)]
    for i in range(days):
        r, c = cells[i]
        grid[r - 1][c - 1] = 1

    # init bfs search
    visited = set()
    queue = deque()
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for c in range(cols):
        if grid[0][c] == 0:
            queue.append([0, c])
            visited.add((0, c))

    while queue:
        r, c = queue.popleft()
        if r == rows - 1:
            return True

        for dr, dc in directions:
            newR, newC = r + dr, c + dc
            if newR < 0 or newR >= rows or newC < 0 or newC >= cols:
                continue
            if (newR, newC) in visited:
                continue
            if grid[newR][newC] == 1:
                continue
            queue.append([newR, newC])
            visited.add((newR, newC))

    return False


def last_day_to_cross(rows, cols, water_cells):
    left, right = 1, len(water_cells)
    while left <= right:
        mid = (left + right) // 2
        if bfs(mid, rows, cols, water_cells):
            left = mid + 1
        else:
            right = mid - 1
    return right
```

### **Accounts merge**

```python
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if x == self.parent[x]:
            return x
        return self.find(self.parent[x])

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False

        if self.size[p1] < self.size[p2]:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]
        else:
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]
        return True


def accountsMerge(accounts):
    uf = UnionFind(len(accounts))
    # email -> Account and union
    emailToAccount = {}

    for i, a in enumerate(accounts):
        for e in a[1:]:
            if e in emailToAccount:
                uf.union(i, emailToAccount[e])
            emailToAccount[e] = i

    # name: email list
    emailList = defaultdict(list)
    for e, i in emailToAccount.items():
        root = uf.find(i)
        emailList[root].append(e)

    # result = name + sorted(list)
    result = []
    for i, emails in emailList.items():
        name = accounts[i][0]
        result.append([name] + sorted(emails))

    return result
```
