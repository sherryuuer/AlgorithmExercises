# There are n rings and each ring is either red, green, or blue. The rings are distributed across ten rods labeled from 0 to 9.

# You are given a string rings of length 2n that describes the n rings that are placed onto the rods. Every two characters in rings forms a color-position pair that is used to describe each ring where:

# The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
# The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').
# For example, "R3G2B1" describes n == 3 rings: a red ring placed onto the rod labeled 3, a green ring placed onto the rod labeled 2, and a blue ring placed onto the rod labeled 1.

# Return the number of rods that have all three colors of rings on them.
# Input: rings = "B0B6G0R6R0R6G9"
# Output: 1
rings = "B0B6G0R6R0R6G9"


def countRods(string):
    ring_list = [char for char in rings]
    # print(ring_list)
    # dict = {}
    dict = {}
    # loop to pop every char
    for i in range(int(len(rings)/2)):
        num = ring_list.pop()
        char = ring_list.pop()
        print(num)
        print(char)
        if num not in dict:
            dict[num] = set()
            dict[num].add(char)
        else:
            dict[num].add(char)
    # print(dict)
    # if num as key,if rgb as values in a set
    count = 0
    for i, v in dict.items():
        if len(v) == 3:
            count += 1
    print(count)
    return count
# with the set count the number of the keys with rgb


# countRods(rings)


# 其他老师解法
def countPoints(s):
    # 宫水三叶
    n, ans = len(s), 0
    map = [0] * 128  # ASCII的最大字符数
    for i in range(0, n, 2):
        map[ord(s[i]) - ord('B')] |= 1 << (int(s[i + 1]) - int('0'))
    print(map)
    for i in range(10):
        tot = 0
        for c in ['R', 'G', 'B']:
            tot += (map[ord(c) - ord('B')] >> i) & 1
        ans += 1 if tot == 3 else 0
    print(ans)
    return ans


countPoints(rings)

# 位掩码（Bitmask）是一种在计算机编程中常用的技术，用于操作和控制二进制位。位掩码是一个整数值，其中的每个二进制位（0或1）都代表一个特定的标志或开关。通过设置或清除位掩码的特定位，可以实现各种操作，如标志的开关、集合的操作和权限的管理。
# 常见的位掩码操作包括：
# 1. 设置位（Setting a Bit）：将特定位设置为1，通常使用按位或运算（`|`）来实现，例如 `mask |= 1 << bit_position` 将 `mask` 的第 `bit_position` 位设置为1。

# 2. 清除位（Clearing a Bit）：将特定位设置为0，通常使用按位与非运算（`&~`）来实现，例如 `mask &= ~(1 << bit_position)` 将 `mask` 的第 `bit_position` 位设置为0。

# 3. 检查位（Checking a Bit）：确定特定位是否为1，通常使用按位与运算（`&`）来实现，例如 `(mask & (1 << bit_position)) != 0` 用于检查 `mask` 的第 `bit_position` 位是否为1。

# 4. 切换位（Toggling a Bit）：将特定位从1切换到0或从0切换到1，通常使用按位异或运算（`^`）来实现，例如 `mask ^= 1 << bit_position` 将 `mask` 的第 `bit_position` 位翻转。

# 位掩码在各种领域的编程中非常有用，包括处理权限、集合操作、状态管理以及优化算法等。它们可以用来表示和操作一组开关或标志，以实现特定的需求。
