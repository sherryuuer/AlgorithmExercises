# 反转一个正整数。

# num = int(input('num = '))  # 345
num = 345
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    # 每次取得num的个位数
    num //= 10
    # 将原来的数字的个位去掉
    # print(reversed_num)
# print(reversed_num)

# 还有没有别的反转方法-字符串反转
num = input("num = ")
reversed_num = ""
for i in range(len(num)-1, -1, -1):
    reversed_num += num[i]
print(int(reversed_num))
