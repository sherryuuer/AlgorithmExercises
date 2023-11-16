# 问一下gpt 辗转相除法，欧几里得算法
# 更相减损术
a = 12
b = 42
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
answer = b
print(answer)
