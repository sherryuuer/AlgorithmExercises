# 8 employees: 0, 1, 2, 3, 4, 5, 6, 7 they are index
from collections import defaultdict
headID = 4
managers = [2, 2, 4, 6, -1, 4, 4, 5]
informTime = [0, 0, 4, 0, 7, 3, 6, 0]
# answer: 13
# thinking: restructure the graph in tree format(no need to go back, so it is directed!),
# and use dfs to calculate the time, get max time of every layer
# steps:
# variable: maxTime = 0
# 1, restructure: {index:[submemberlist]}
# 2, dfs -> get the time -> update the max time
# return maxTime


def dfs(adjList, node, curTime, informTime):
    """dfs is not easy to image in head"""
    if not adjList[node]:
        return curTime

    maxTime = curTime
    for member in adjList[node]:
        maxTime = max(maxTime, dfs(adjList, member,
                      curTime + informTime[node], informTime))

    return maxTime


def timeNeededToInform(managers, headID, informTime):
    if headID == 0 and len(manager) == 1:
        return 0
    adjList = defaultdict(list)
    for employeeId, manager in enumerate(managers):
        if manager != -1:
            adjList[manager].append(employeeId)

    print(adjList)

    return dfs(adjList, headID, 0, informTime)


print(timeNeededToInform(managers, headID, informTime))
# Time O(n) Space O(n)
