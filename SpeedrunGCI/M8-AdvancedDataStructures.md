## Graphs
- Relationships between elements

**Pacific Atlantic Water Flow**

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

## Trie
1. Partial matches
2. Space optimization
3. Can break down the string

**Implement Trie (Prefix Tree)**
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
