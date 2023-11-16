import heapq  # 使用python的堆数据模块
# Probleme
# 25人进行5人一组的比赛，决出前三名，最少可以比几轮决出
# 结论是7
# 实质是二叉树bfs问题
# A = {"A1": 25, "A2": 24, "A3": 19, "A4": 16, "A5": 18, }
# B = {"B1": 23, "B2": 20, "B3": 18, "B4": 17, "B5": 16, }
# C = {"C1": 22, "C2": 14, "C3": 13, "C4": 12, "C5": 11, }
# D = {"D1": 10, "D2": 9, "D3": 8, "D4": 7, "D5": 6, }
# E = {"E1": 5, "E2": 4, "E3": 3, "E4": 2, "E5": 1, }
A = [25, 24, 19, 16, 18]
B = [23, 20, 18, 17, 16]
C = [22, 14, 13, 12, 11]
D = [10, 9, 8, 7, 6]
E = [5, 4, 3, 2, 1]
# 先比五轮
# 第六轮由各组第一决出最终第一
# 第七轮无人决定方法：
# 可能得第二的是，被第一打败的B1和A2
# 可能得第三的是，被B1打败的C1和B2，以及被A2打败的A3
# 这五人再比一次决出2，3名，一共是7次。
# for n in (A, B, C, D, E):
#     print(f"n = {[v for v in n.values()]}")


# 5 loops for all team
def loop_contest(team=A):
    heapq.heapify(team)
    winnerlist = []
    for i in range(5):
        winnerlist.append(heapq.heappop(team))
    return winnerlist[::-1]  # reverse


loop1 = loop_contest(A)
print("loop1")
print(loop1)
loop2 = loop_contest(B)
print("loop2")
print(loop2)
loop3 = loop_contest(C)
print("loop3")
print(loop3)
loop4 = loop_contest(D)
print("loop4")
print(loop4)
loop5 = loop_contest(E)
print("loop5")
print(loop5)


loops = [loop1, loop2, loop3, loop4, loop5]
# loop 6 to get the hightest
loop6 = []
for loop in loops:
    loop6.append(loop[0])
print("loop6")
print(loop6)

heapq.heapify(loop6)
NO1, P1, P2 = heapq.nlargest(3, loop6)

print(f"NO1 is {NO1},the highest of loop6")

# 准备进行第七轮的人
loop7 = [P1, P2]  # 在loop6中输给第一名的两人直接进入决赛
for loop in loops:
    if NO1 in loop:
        loop7.append(loop[1])
        loop7.append(loop[2])
    if P1 in loop:
        loop7.append(loop[1])
print("loop7")
print(loop7)

# last contest
heapq.heapify(loop7)
NO2, NO3 = heapq.nlargest(2, loop7)
print(f"NO2 is {NO2},the first of loop7")
print(f"NO3 is {NO3},the second of loop7")
