## Two Pointers
1. Linear data structure
2. Process pairs
3. Dynamic pointer movement

### **3Sum problem**
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
### **Container with Most Water**
```python
def container_with_most_water(height):
    if not height:
        return 0
    max_amount = 0 # space O(1)

    left, right = 0, len(height) - 1
    while left <= right: # time O(n)
        # calculate the sum [0, 1, 2, 3]
        cur_sum = (right - left) * min(height[left], height[right])
        # get the new max
        max_amount = max(max_amount, cur_sum)
        # move the pointer: move the shorter one
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_amount
```

### **Trapping Rain Water**
- this is a hard problem, don't dispoint on this
```python
def rain_water(heights):
    left, right = 0, len(heights) - 1
    maxL, maxR = 0, 0
    total_water = 0

    while left < right:
        if heights[left] < heights[right]:
            if heights[left] > maxL:
                maxL = heights[left]
            else:
                total_water += maxL - heights[left]
            left += 1

        else:
            if heights[right] > maxR:
                maxR = heights[right]
            else:
                total_water += maxR - heights[right]
            right -= 1

    return total_water
```



## Modified Binary Search
1. Target value in sorted data
2. Partially sorted segments
3. sorted is the keyword

### **Search in Rotated Sorted Array**
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

### **Random Pick with Weight**

这道题其实我一开始很费解。

“Random Pick with Weight” 这道题背后的核心原理是 **加权概率分布（Weighted Probability Distribution）**，即根据每个元素的权重大小来影响其被选中的概率。这个原理在许多概率与统计应用中被广泛使用，比如在抽奖、加权投票、负载均衡等场景中，通过权重实现不同对象的选择概率。

1. **概率分布（Probability Distribution）**：
   - 在这道题中，每个权重 `w[i]` 可以看作元素 `i` 被选中的“相对概率”。具体来说，`i` 被选中的概率是 `w[i] / sum(w)`。
   - 例如，如果 `w = [1, 3, 2]`，总权重为 `1 + 3 + 2 = 6`。那么，第一个元素被选中的概率就是 `1/6`，第二个是 `3/6`，第三个是 `2/6`。

2. **区间划分（Range Partitioning）**：
   - 为了实现这种概率分布，我们可以把区间 `[0, sum(w))` 划分为与 `w` 中每个元素成比例的子区间。比如在 `w = [1, 3, 2]` 的例子中，总权重为 6，我们可以分成如下区间：
     - 元素 0：`[0, 1)`，长度为 1。
     - 元素 1：`[1, 4)`，长度为 3。
     - 元素 2：`[4, 6)`，长度为 2。
   - 因此，生成一个在 `[0, 6)` 范围内的随机数 `r`，根据 `r` 所在的区间选择对应的索引，就能实现不同概率的选择。

3. **前缀和数组（Prefix Sum Array）**：
   - 为了快速找到随机数 `r` 所属的区间，我们可以使用一个前缀和数组。前缀和数组的每一项表示从第一个元素到当前元素的累积权重。例如，在 `w = [1, 3, 2]` 中，前缀和数组为 `[1, 4, 6]`。
   - 当生成随机数 `r` 后，我们可以通过 **二分查找** 在前缀和数组中快速找到第一个大于 `r` 的元素位置。这一步的复杂度是 `O(log n)`，大大提高了效率。

“Random Pick with Weight” 的核心在于利用加权概率分布和前缀和数组，将权重转换为区间长度，实现了加权随机选择。每个元素的权重越大，它的区间越长，被随机选中的概率也越高。

```python
import random


class RandomPickWithWeight:

    def __init__(self, weights):
        self.prefix_sums = []
        self.total = sum(weights)
        former_sum = 0
        for w in weights:
            current_sum = former_sum + w
            self.prefix_sums.append(current_sum)
            former_sum = current_sum

    def pick_index(self):
        # Replace this placeholder return statement with your code
        target = random.uniform(0, self.total)
        L, R = 0, len(self.prefix_sums) - 1

        while L <= R:
            mid = (L + R) // 2
            if self.prefix_sums[mid] > target:
                if mid == 0 or self.prefix_sums[mid - 1] <= target:
                    return mid
                R = mid - 1
            else:
                L = mid + 1
        return -1
```
