## Merge Intervals
1. Array of intervals
2. Overlapping intervals

- **Merge Intervals**
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

## K-way Merge
1. an expansion of the standard merge sort
2. Involves merging sorted arrays or a matrix
3. Seeking the kth smallest/largest across sorted collections

**Merge Sorted Array**
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
