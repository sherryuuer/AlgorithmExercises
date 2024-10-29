## Two Pointers
1. Linear data structure
2. Process pairs
3. Dynamic pointer movement

- **3Sum problem**
```python
def find_sum_of_three(nums, target):
    nums.sort() # space O(n)

    for i in range(len(nums)): # time O(n^2)
        left, right = i + 1, len(nums) - 1
        subTarget = target - nums[i]

        while left < right:
            if nums[left] + nums[right] == subTarget:
                return True
            elif nums[left] + nums[right] < subTarget:
                left += 1
            else:
                right -= 1
    return False
```

## Modified Binary Search
1. Target value in sorted data
2. Partially sorted segments
3. sorted is the keyword

- **Search in Rotated Sorted Array**
```python
def binary_search_rotated(nums, target):
    low, high = 0, len(nums) - 1 # space O(1)

    while low <= high:
        mid = (low + high) // 2 # time O(logn)
        if nums[mid] == target:
            return mid

        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        elif nums[mid] <= nums[high]:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1
```
