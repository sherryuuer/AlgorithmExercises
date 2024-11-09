## Graphs
- Relationships between elements

### **Pacific Atlantic Water Flow**

```python
def estimate_water_flow(heights):
    ROWS = len(heights)
    COLS = len(heights[0])

    def dfs(row, col, result): # time O(m * n) space O(m * n)
        result.add((row, col))

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for dr, dc in directions:
            newRow, newCol = row + dr, col + dc
            if newRow < 0 or newRow >= ROWS or newCol < 0 or newCol >= COLS:
                continue
            if (newRow, newCol) in result:
                continue
            if heights[row][col] > heights[newRow][newCol]: # 这里要找的是比出发点高的，因为我们在反向找
                continue

            dfs(newRow, newCol, result)

    resultP = set()
    resultA = set()

    for r in range(ROWS):
        dfs(r, 0, resultP)         # left
        dfs(r, COLS - 1, resultA)  # right
    for c in range(COLS):
        dfs(0, c, resultP)         # up
        dfs(ROWS - 1, c, resultA)  # down

    return list(resultP & resultA)
```

### **Reconstruct Itinerary**
```python
def find_itinerary(tickets):
    adj = { src: [] for src, dst in tickets }

    tickets.sort()
    for src, dst in tickets:
        adj[src].append(dst)

    result = ["JFK"]
    def dfs(src):
        if len(result) == len(tickets) + 1:
            return True
        if src not in adj:
            return False

        temp = adj[src]
        for i, v in enumerate(temp):
            adj[src].pop(i)
            result.append(v)

            if dfs(src): return True

            adj[src].insert(i, v)
            result.pop()

        return False

    dfs("JFK")
    return result

```

## Trie
1. Partial matches
2. Space optimization
3. Can break down the string

### **Implement Trie (Prefix Tree)**
```python
class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    # inserting string in trie
    def insert(self, string): # time O(n) space O(n)
        cur = self.root
        for c in string:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

    # searching for a string
    def search(self, string): # time O(n) space O(1)
        cur = self.root
        for c in string:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.is_word

    # searching for a prefix
    def search_prefix(self, prefix): # time O(n) space O(1)
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
```

### **Top K Frequent Words**
- 不考虑trie的方法，则用python进行字典count和排序即可, 但是根据字典的大小，时间复杂度会很高
`sorted_data = sorted(data.items(), key=lambda x: (-x[1], x[0]))`
- 这题用trie加桶排序的代码复杂度很高，我更偏向于heapq方法
```python
from collections import Counter
import heapq

def topKFrequent(words, k):
    # 统计单词频率
    count = Counter(words)

    # 构建小顶堆
    heap = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(heap)

    # 获取前 K 个频率最高的单词
    result = [heapq.heappop(heap)[1] for _ in range(k)]

    return result
```

## Custom Data Structures
1. Modification of an existing data structure
2. Multiple data structures involved

**Snapshot Array**
```python
class SnapshotArray:
    # Constructor
    def __init__(self, length):
        self.array = [0] * length
        self.curid = -1
        self.snapshots = {}

    # Function set_value sets the value at a given index idx to val.
    def set_value(self, idx, val):
        if idx >= len(self.array):
            return
        self.array[idx] = val

    # This function takes no parameters and returns the snapid.
    # snapid is the number of times that the snapshot() function was called minus 1.
    def snapshot(self):
        self.curid += 1
        self.snapshots[self.curid] = self.array[:]
        return self.curid

    # Function get_value returns the value at the index idx with the given snapid.
    def get_value(self, idx, snapid):
        if idx >= len(self.array) or snapid > self.curid:
            return -1
        return self.snapshots[snapid][idx]

# above is quite not efficient, we need some system like version control
from collections import defaultdict
import copy

# space O(n * m)
class SnapshotArray:
    # Constructor
    def __init__(self, length):
        self.curid = 0
        self.length = length
        self.snapshots = defaultdict(dict) # {snapid: {idx: val}} 设计自己的数据结构 cool

    # Function set_value sets the value at a given index idx to val.
    def set_value(self, idx, val): # time O(1), space O(1)
        if idx >= self.length:
            return
        self.snapshots[self.curid][idx] = val

    # This function takes no parameters and returns the snapid.
    # snapid is the number of times that the snapshot() function was called minus 1.
    def snapshot(self): # time O(n) space O(n)
        self.curid = self.curid + 1
        self.snapshots[self.curid] = copy.deepcopy(self.snapshots[self.curid - 1])
        return self.curid - 1

    # Function get_value returns the value at the index idx with the given snapid.
    def get_value(self, idx, snapid): # time O(1) space O(1)
        if idx >= self.length or snapid > self.curid:
            return

        return self.snapshots.get(snapid).get(idx, 0)
```

### **LRU cache**
- set
1. Check if it cache:
2. in -> update cache, remove and insert list
3. not in -> add to cache, insert list
4. Check the capacity -> remove the first node from cache and list

```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity,):
        self.capacity = capacity
        self.cache = {} # for repidly search key: node
        self.left = Node(0, 0) # linked list left dummy node
        self.right = Node(0, 0) # linked list right dummy node
        self.left.next = self.right
        self.right.prev = self.left

    def _insert_to_queue(self, node):
        p, n = self.right.prev, self.right
        node.prev, node.next = p, n
        p.next = n.prev = node

    def _remove_from_queue(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p

    def get(self, key):
        if key in self.cache:
            # deal with the linked list
            self._remove_from_queue(self.cache[key])
            self._insert_to_queue(self.cache[key])
            return self.cache[key].value
        return -1 # ask if this is ok or should I return None

    def set(self, key, value):
        if key in self.cache:
            self._remove_from_queue(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert_to_queue(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self._remove_from_queue(lru)
            del self.cache[lru.key]
```

### **Insert Delete GetRandom O(1)**
- init: hashmap {val: index} array []
- insert:
  - if not in hashmap, append array add to hashmap, return true
  - if in hashmap, return false
- delete:
  - if in hashmap, delete idx = hashmap[val], add {array[-1]: idx} to hashmap, array.pop()
  - if not in hashmap, return false
- get random:
  - return random.choice(array)

```python
import random


class RandomSet():

    def __init__(self):
        self.hashmap = {}
        self.array = []

    def insert(self, val):
        if val not in self.hashmap:
            self.array.append(val)
            self.hashmap[val] = len(self.array) - 1
            return True
        return False

    def delete(self, val):
        if val in self.hashmap:
            idx = self.hashmap[val]
            self.hashmap[self.array[-1]] = idx
            self.array[idx] = self.array[-1]
            self.array.pop()
            del self.hashmap[val]
            return True
        return False

    def get_random(self):
        return random.choice(self.array)
```

### **Range Module**

```python
from bisect import bisect_left, bisect_right

class RangeModule:
    def __init__(self):
        self.intervals = []

    def add_range(self, left, right):  # 这个merge的逻辑很妙，比我之前写的更加聪明
        new_intervals = []
        i = 0
        while i < len(self.intervals) and self.intervals[i][1] < left:
            new_intervals.append(self.intervals[i])
            i += 1

        while i < len(self.intervals) and self.intervals[i][0] <= right:
            left = min(left, self.intervals[i][0])
            right = max(right, self.intervals[i][1])
            i += 1
        new_intervals.append((left, right))

        while i < len(self.intervals):
            new_intervals.append(self.intervals[i])
            i += 1

        self.intervals = new_intervals

    def query_range(self, left, right):
        i = bisect_right(self.intervals, (left, float('inf'))) - 1
        return i >= 0 and self.intervals[i][0] <= left and self.intervals[i][1] >= right

    def remove_range(self, left, right):
        new_intervals = []
        for interval in self.intervals:
            if interval[1] <= left or interval[0] >= right:
                new_intervals.append(interval)
            else:
                if interval[0] < left:
                    new_intervals.append((interval[0], left))
                if interval[1] > right:
                    new_intervals.append((right, interval[1]))
        self.intervals = new_intervalss
```
