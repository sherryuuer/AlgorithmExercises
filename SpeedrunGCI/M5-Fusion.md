## Merge Intervals
1. Array of intervals
2. Overlapping intervals

### **Merge Intervals**
- steps:
- variables: result(list)
1. loop the intervals list
2. check if overlapping
   - yes: merge them and add to the result list
   - no: just add the curr list into result list
3. return the result list

```python
def overlapping(interval1, interval2):
    return interval1[1] >= interval2[0]

def merge(interval1, interval2):
    left = min(interval1[0], interval2[0])
    right = max(interval1[1], interval2[1])
    return [left, right]

def merge_intervals(intervals):
    result = [] # O(n)

    for interval in intervals: # time O(n)
        if result and overlapping(result[-1], interval):
            poped = result.pop()
            result.append(merge(poped, interval))
        else:
            result.append(interval)

    return result

# handly test
# case = [[1, 5], [3, 7], [4, 6]]
# result = [[1, 5]]
```

### **Insert Interval**
- nonoverlapping and sorted
- steps: how I thinking
1. at head, or at last, if not exsiting_intervals return the cur list
2. result = []
3. loop the list for left, right, use while
   - target is new interval
   - L >= left and R <= right: target = None break
   - R < left: add target and target = None break
   - L > right: add cur and continue
   - others: target = [min(left, L), max(right, R)]

4. return the result + exsiting_intervals[index]

```python
existing_intervals = [[1,2],[3,4],[5,8],[9,15]]
new_interval = [2,5]

def insert_interval(existing_intervals, new_interval):
    """
    Insert a new interval to a existing intervals list
    without overlapping

    args:
        existing_intervals (list[list]): intervals list to be merge and insert
        new_interval ([list]): interval to be merge and insert

    return:
        ([list[list]]): merged and inserted intervals list
    """
    if not existing_intervals:
        return [new_interval]

    target = new_interval
    result = []
    index = 0

    while index < len(existing_intervals):
        L, R = target
        left, right = existing_intervals[index]

        # no need to merge
        if L >= left and R <= right:
            return result + existing_intervals[index:]

        # not overlapping and just add target
        if R < left:
            result.append(target)
            break

        # not overlapping
        if L > right:
            result.append(existing_intervals[index])
            index += 1
            continue

        target = [min(left, L), max(right, R)]
        index += 1

    # edge case: target add to last
    if not result or target[0] > result[-1][1]:
        result.append(target)

    return result + existing_intervals[index:]
```
- time: O(n), n = len(existing_intervals)
- space: O(n) can be optimized to O(1)

### **Employee Free Time**
```python
import heapq


def employee_free_time(schedule):
    intervals = [interval for lst in schedule for interval in lst]
    heapq.heapify(intervals) # 这里并没有变化可以直接排序

    result = []
    _, end = heapq.heappop(intervals)
    while intervals:
        start_time, end_time = heapq.heappop(intervals)
        if start_time <= end:
            end = end_time
            continue
        result.append([end, start_time])
        end = end_time

    return result
```

- 只用sort即可
```python
def employee_free_time(schedule):
    intervals = [interval for lst in schedule for interval in lst]
    intervals = sorted(intervals, key=lambda x: x[0])

    result = []
    _, prev_end = intervals[0]

    for i in range(1, len(intervals)):
        start, end = intervals[i]
        if start > prev_end:
            result.append([prev_end, start])
            prev_end = end
            continue

        prev_end = max(prev_end, end)

    return result
```

### **Meeting Rooms II**
- rooms = [[end_time, room_num]] use a minheap to get the earliest end time
- loop meetings and update the rooms
- count the rooms

```python
import heapq


def find_sets(intervals):
    if not intervals:
        return 0

    intervals = sorted(intervals, key=lambda x: x[0])
    room_num = 1
    rooms = [[0, 1]] # empty_time, room_num

    for interval in intervals: # time O(n)
        heapq.heapify(rooms) # time O(logR)
        empty_time, _ = rooms[0]

        start, end = interval
        if start >= empty_time:
            rooms[0][0] = end
            continue

        room_num += 1
        rooms.append([end, room_num])

    return room_num
```


## K-way Merge
1. an expansion of the standard merge sort
2. Involves merging sorted arrays or a matrix
3. Seeking the kth smallest/largest across sorted collections

### **Merge Sorted Array**
- the key point is You have to modify nums1 in place.

- maybe I can do it *from back to the beginning*
```python
def merge_sorted(nums1, m, nums2, n):
    if not nums1:
        return nums2
    if not nums2:
        return nums1

    p1 = m - 1 # the last element of nums1
    p2 = n - 1 # the last element of nums2
    pointer = m + n - 1

    while p1 >= 0 and p2 >= 0: # time O(m + n) space O(1)
        if nums1[p1] >= nums2[p2]:
            nums1[pointer], nums1[p1] = nums1[p1], nums1[pointer]
            p1 -= 1
        else:
            nums1[pointer], nums2[p2] = nums2[p2], nums1[pointer]
            p2 -= 1
        pointer -= 1

    while p2 >= 0:
        nums1[pointer], nums2[p2] = nums2[p2], nums1[pointer]
        p2 -= 1
        pointer -= 1

    return nums1
```

### **Merge K Sorted Lists**

```python
from linked_list import LinkedList
from linked_list_node import LinkedListNode

def merge_2_lists(head1, head2):
    dummy = LinkedListNode(-1)
    prev = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            prev.next = head1
            head1 = head1.next
        else:
            prev.next = head2
            head2 = head2.next
        prev = prev.next

    if head1 is not None:
        prev.next = head1
    else:
        prev.next = head2

    return dummy.next


# Main function
def merge_k_lists(lists):
    if len(lists) > 0:
        step = 1
        while step < len(lists):
            for i in range(0, len(lists) - step, step * 2):
                lists[i].head = merge_2_lists(lists[i].head, lists[i + step].head)
            step *= 2
        return lists[0].head
    return
```
