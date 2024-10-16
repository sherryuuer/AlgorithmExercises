# There are total of n courses 0 ~ n - 1
# and a array list of prerequisite pairs, [1, 0] means if you want to take course 1
# you must take course 0 first, means 0 -> 1
# find out if all courses can be completed

# Constraints:
# Can it have seperate graphs? yes

from collections import defaultdict, deque
numCourses1 = 2
prerequisites1 = [[1, 0]]
# true
numCourses2 = 2
prerequisites2 = [[1, 0], [0, 1]]
# false
numCourses3 = 6
prerequisites3 = [[1, 0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]]
# 3 -> 0 -> 1 -> 2
#   -> 4    5 -> 2
#             -> 3
# true
# so we need to find out if it has cycle!!


def dfs(adjList, course, path, completed):
    if course in path:
        return False
    if course in completed:
        return True

    path.add(course)
    for next in adjList[course]:
        if not dfs(adjList, next, path, completed):
            return False

    completed.append(course)
    path.remove(course)

    return True


def courseSchedulerDFS(numCourses, prerequisites):
    adjList = defaultdict(list)
    for n in range(numCourses):
        adjList[n]

    for pre in prerequisites:
        adjList[pre[1]].append(pre[0])

    completed = []  # for traversal

    for course in range(numCourses):
        path = set()
        if not dfs(adjList, course, path, completed):
            return False

    return True


print(courseSchedulerDFS(numCourses3, prerequisites3))


# 拓扑排序用于DAG，每个节点都有待处理的前置节点，称为degree，如果degree归零，意味着这个节点可以被处理，直到最后
# 下面这个方法使用了stack，我觉得queue也可以
def topologicalCourseScheduler(numCourse, prerequisites):
    adjList = {}
    for n in range(numCourse):
        adjList[n] = []

    inDegree = [0 for _ in range(numCourse)]

    for pre in prerequisites:
        adjList[pre[1]].append(pre[0])
        inDegree[pre[0]] += 1

    # stock the 0 degree (the course that can be process)
    stack = []
    for course, degree in enumerate(inDegree):
        if degree == 0:
            stack.append(course)
    # count the processed courses
    count = 0

    while stack:
        curCourse = stack.pop()
        count += 1
        nextCourse = adjList[curCourse]

        for c in nextCourse:
            inDegree[c] -= 1
            if inDegree[c] == 0:
                stack.append(c)

    # if all the courses all processed, return true
    return count == numCourse


print(topologicalCourseScheduler(numCourses3, prerequisites3))


def courseScheduler(numCourses, prerequisites):
    """Solve in queue"""
    # Step 1: Build the adjacency list and in-degree array
    adjList = defaultdict(list)
    inDegree = [0] * numCourses

    for pre in prerequisites:
        adjList[pre[1]].append(pre[0])
        # Increase in-degree for the course with prerequisites
        inDegree[pre[0]] += 1

    # Step 2: Initialize the queue with nodes having in-degree 0
    queue = deque([course for course in range(
        numCourses) if inDegree[course] == 0])

    # Count of processed courses
    processed_courses = 0

    # Step 3: Process the queue (BFS)
    while queue:
        current_course = queue.popleft()
        processed_courses += 1  # Mark this course as processed

        # Step 4: Reduce the in-degree of neighbors and add those with in-degree 0 to the queue
        for next_course in adjList[current_course]:
            inDegree[next_course] -= 1
            if inDegree[next_course] == 0:
                queue.append(next_course)

    # Step 5: If we've processed all courses, there's no cycle, otherwise there is a cycle
    return processed_courses == numCourses
