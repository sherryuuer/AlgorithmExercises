# graph relation
graph = dict()
graph["start"] = {"a": 6, "b": 2}
graph["a"] = {"fin": 1}
graph["b"] = {"a": 3, "fin": 5}
graph["fin"] = {}

# cost dict
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# parent dict
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

print(f"the map: {graph}")
print("-------------------------")
print(f"the costs: {costs}")
print("-------------------------")
print(f"the parents: {parents}")
print("-------------------------")

# to memo the node have been processed.
processed = []


def find_lowest_cost_node(costs):
    '''
    function to find the minnest value's key of the costs dict.
    if the node in processed list ,it will not be choose.
    parameters: costs
    '''
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost_node = node
            lowest_cost = cost
    return lowest_cost_node


# 1,find the lowest cost node
node = find_lowest_cost_node(costs)
# print(node)

while node is not None:
    cost = costs[node]  # 2,get the node's costs and neighbors
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:  # update the cost if the new cost is lower than the old cost.
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

# print(costs)
# print(parents)

reversed_roote = ["fin"]
for i in range(len(parents)):
    reversed_roote.append(parents[reversed_roote[-1]])
route = reversed_roote[::-1]
print(f"Found the shortest route! that is {route}")


# 狄克斯特拉算法
# 1，找到start节点后最便宜的节点
# 2，找到该节点的所有邻居，尝试更新他们的最便宜权值，同时更新父节点
# 3，处理完后将该节点冻结不再使用
# 4，重复以上步骤直到处理完所有节点
