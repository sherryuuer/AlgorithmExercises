# 集合覆盖问题
# 算法图解
# 美国广播覆盖问题
# 贪心算法
# states
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
# broadcasts
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    final_stations.add(best_station)
    states_needed -= states_covered

print(final_stations)
# 其实是一个不断优化局部最优解的过程
# O(n^2)
# n + (n - 1) + (n - 2) + ... + 1 = n * (n + 1) / 2 = n^2
# 精确计算的复杂度是O(2^n)  每个电台有选或者不选两个选项
