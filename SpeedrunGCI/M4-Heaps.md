## Top K Elements
1. Unsorted list analysis
2. The goal is to identify a subset rather than just a single extreme value.
   - top k, kth largest/smallest, k most frequent, k closest, or k highest/lowest

### **Reorganize String**

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

### **Kth Largest Element in an Array**
- 这种问题基本上是暴力解法用排序算法先排序，然后找到对应元素
- 使用堆进行算法优化
```python
import heapq


def find_kth_largest(nums, k):
    if not nums:
        return -1

    min_heap = [] # space O(k)

    for i, n in enumerate(nums): # time O(nlogn)
        if i < k:
            heapq.heappush(min_heap, n)
        elif n > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, n)
        else:
            continue

    return min_heap[0]
```


## Two Heaps
1. Static or streaming data：静态或者动态数据
2. *Maxima and minima* calculation：要计算最大最小

### **Find Median from Data Stream**
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

### **Meeting Rooms III**
- steps: bruteforce
- hashmap: {room: counter}, {room: empty time}
- loop the meetings array for each meeting find the room for it
  - loop the room to find a empty one, update the counter and next empty time for the room
- return the room with biggest counter value
- I have solution but may be it is not a best one
- how to determine the best solution

- 两个堆方法：
- free room heap [0, 1, 2, ...], in_use heap [(empty_time, room_num)]
- sort the meetings and loop for it
  - check the in_use heap index 0, get the (empty time is early than the meeting)value from it put it into the free room
  - get a free room for the meeting and put it into in use, update the counter
- return the room num with biggest value

```python
import heapq
meetings = [[0, 1], [2, 4], [3, 6]]
rooms = 2
def most_booked(meetings, rooms):
    if not meetings:
        return 0
    room_counter = {n: 0 for n in range(rooms)}
    free_room = [n for n in range(rooms)] # space O(room)
    in_use = [] # [empty_time, room_num]
    meetings.sort()

    for start, end in meetings: # time O(m * logn)
        while in_use and in_use[0][0] <= start:
            _, room = heapq.heappop(in_use)
            heapq.heappush(free_room, room)

        if not free_room: # 这里我一开始出了问题，是因为没有将题意读清楚！！
            # with for the room in in_use
            empty_time, room_num = heapq.heappop(in_use)
            end = empty_time + (end - start)
            heapq.heappush(free_room, room_num)

        use_room = heapq.heappop(free_room)
        heapq.heappush(in_use, [end, use_room])
        room_counter[use_room] += 1

    return max(room_counter.items(), key=lambda item: (item[1], -item[0]))[0]
# passed with simple testcase，but failed some case
```
- 读清楚每一个题意！
