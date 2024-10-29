## Top K Elements
1. Unsorted list analysis
2. The goal is to identify a subset rather than just a single extreme value.
   - top k, kth largest/smallest, k most frequent, k closest, or k highest/lowest

**Reorganize String**

```python
# test cases
case1 = "aaabc" # abaca a3,b1,c1
case2 = "abaacdda" # adadacab a4,d2,b1,c1 adadabac
case3 = "aaab" # "" a2,b0 aba if only 1 element it must not be 2
```

step:
- bruteforce:
  1. create Counter
  2. loop to find a element not equal the former one, count--


- top k elemnt
  1. Counter hashmap
  2. count_list like [count, element]
  3. heapq get 2 element, add the most one, count-=1
- time O(nlog26) space O(26)->O(1)
```python
from collections import Counter
import heapq


def reorganize_string(str):
    result = ""
    # test "abb"
    count_map = Counter(str) # space O(26) -> O(1)
    count_list = [[-v, k] for k, v in count_map.items()] # [-1, "a"], [-2, "b"]
    heapq.heapify(count_list)

    while len(count_list) >= 2: # time O(n)
        char1 = heapq.heappop(count_list) # b
        char2 = heapq.heappop(count_list) # a

        if not result:
            result += char1[1]
            result += char2[1]
        else:
            if result[-1] != char1[1]:
                result += char1[1]
                result += char2[1]
            else:
                result += char2[1]
                result += char1[1]

        char1[0] += 1
        char2[0] += 1

        if char1[0] != 0:
            count_list.append(char1)
        if char2[0] != 0:
            count_list.append(char2)

        heapq.heapify(count_list)

    if len(count_list) == 1 and count_list[0][0] == -1:
        result += count_list[0][1]
        return result
    elif len(count_list) == 1 and count_list[0][0] < -1:
        return ""
    else:
        return result
```

- backtracking
  1. variables: map, "", res

```python
from collections import Counter


def backtrack(path, count_map, length):
    if len(path) == length:
        return "".join(path)

    for char in count_map:
        if count_map[char] > 0 and (not path or path[-1] != char):
            path.append(char)
            count_map[char] -= 1

            result = backtrack(path, count_map, length)
            if result:
                return result

            path.pop()
            count_map[char] += 1

    return None

def reorganize_string(str):
    path = []
    count_map = Counter(str)
    result = backtrack(path, count_map, len(str))
    return result if result else ""
```
- 这里为了练习，学习到了要给出最终的return和进行pop，虽然效率很低，但是coding起来还是很快乐的

## Two Heaps
1. Static or streaming data：静态或者动态数据
2. *Maxima and minima* calculation：要计算最大最小

**Find Median from Data Stream**
- min heap keep the bigger side
- max heap keep the smaller side
```python
import heapq

class MedianOfStream:
    def __init__(self):
        self.large = [] # min heap
        self.small = [] # max heap

    def insert_num(self, num): # time O(log) space O(n)
        heapq.heappush(self.small, -1 * num)

        # deal with the pushed val
        if self.large and self.small and self.small[0] * -1 > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # deal with the balance
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)
        elif len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

    def find_median(self): # time O(1) space O(n)
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.small) > len(self.large):
            return self.small[0] * -1
        return (self.large[0] + (-1 * self.small[0])) / 2.0
```
