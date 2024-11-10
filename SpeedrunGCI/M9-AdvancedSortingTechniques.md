## Cyclic Sort
1. Limited range: array should not be too long
2. Not stable
3. Not suitable for noninteger arrays
4. Not suitable when multiple attributes play a significant role

- I think this problem is about *swap* and *check*
**First Missing Positive**
```python
def smallest_missing_positive_integer(nums):
    # time O(n)
    for i in range(len(nums)):
        rightSpot = nums[i] - 1

        while 1 <= nums[i] <= len(nums) and nums[i] != nums[rightSpot]:
            # space O(1)
            nums[i], nums[rightSpot] = nums[rightSpot], nums[i]
            rightSpot = nums[i] - 1

    for i in range(len(nums)):
        if nums[i] != (i + 1):
            return i + 1

    return len(nums) + 1
```


## Topological Sort
1. Dependency relationships
2. Ordering or sequencing

## **Course Schedule**

```python
prerequisites = [[1, 0], [1, 2], [3, 1], [4, 1], [1, 4], [5, 1]]
num_courses = 6
from collections import defaultdict
def can_finish(num_courses, prerequisites):
    # indegress map {node : indegress}
    indegress = {}
    for c in range(num_courses):
        indegress[c] = 0
    for c, p in prerequisites:
        indegress[c] += 1

    stack = []
    for c, degress in indegress.items():
        if degress == 0:
            stack.append(c)

    adjList = defaultdict(list)
    for c, p in prerequisites:
        adjList[p].append(c)

    finished = 0
    while stack:
        course = stack.pop()
        finished += 1
        # reduce degree for courses the after this course
        for c in adjList[course]:
            indegress[c] -= 1
            if indegress[c] == 0:
                stack.append(c)

    return finished == num_courses
```
- all the vertices and edges are stored in a adjList and looped by once, so O(V + E)

## **Course Schedule**

```python
def find_order(num_courses, prerequisites):
    in_degress = { c: 0 for c in range(num_courses) }
    adj = { c: [] for c in range(num_courses) }

    for c, p in prerequisites:
        in_degress[c] += 1
        adj[p].append(c)

    stack = []
    for c, d in in_degress.items():
        if d == 0:
            stack.append(c)

    take_courses = []
    while stack:
        course = stack.pop()
        take_courses.append(course)

        for c in adj[course]:
            in_degress[c] -= 1
            if in_degress[c] == 0:
                stack.append(c)

    return take_courses if len(take_courses) == num_courses else []
```
