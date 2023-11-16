# 田忌赛马问题
horses_tianji = [3, 6, 8, 10]
horses_qiwang = [2, 7, 9, 11]


def maximize_wins(horses_tianji, horses_qiwang):
    if not horses_tianji or not horses_qiwang:
        return 0  # 没有马可比赛

    # 选择齐王的一匹马
    qiwang_horse = horses_qiwang[0]
    print("qiwang", qiwang_horse)
    # 找到田忌的马中可以击败齐王的最慢的一匹马
    tianji_horse = min(filter(lambda x: x > qiwang_horse, horses_tianji), default=None)
    print("tianji", tianji_horse)
    # 如果找到了，田忌胜利，分数加一，并递归处理剩余的马匹
    if tianji_horse is not None:
        return 1 + maximize_wins([x for x in horses_tianji if x != tianji_horse], horses_qiwang[1:])
    else:
        # 如果找不到可以击败的马，田忌选择一匹自己的最慢马进行比赛
        return maximize_wins(horses_tianji[1:], horses_qiwang[1:])


max_wins = maximize_wins(horses_tianji, horses_qiwang)
print("最大胜利场次:", max_wins)
