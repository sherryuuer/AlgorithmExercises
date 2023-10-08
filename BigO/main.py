# Big O rules:
# 1,Worst case
# 2,Remove constants O(n)
# 3,Different terms for inputs O(m + n)
# 4,Drop Non dominants

# Data Structures + Algorithms = Programs
# readable & scalable
# Time and Space scala

# O(n^2)
boxs = [1, 2, 3, 4, 5]
for i in range(len(boxs)):
    a = boxs[i]
    for j in range(i + 1, len(boxs)):
        b = boxs[j]
        print(a, b)


#######################################################################
# import datetime


# nemo = ["nemo"]
# everyone = ["dory", "bruce", "marlin", "nemo", "gill", "bloat", "nigel", "squirt", "darla", "hank"]
# large = ["nemo" for i in range(10000)]
# # print(large)


# def function(list):
#     t0 = datetime.datetime.now()
#     i = 0
#     for i in range(len(list)):
#         if list[i] == "nemo":
#             print("Found nemo!")
#             break
#         i += 1
#     t1 = datetime.datetime.now()
#     print(t1 - t0)


# function(large)  # O(n)
#######################################################################

# def anotherFunction():
#     pass


# def funChallenge(input):
#     a = 10  # O(1)
#     a = 50 + 3

#     for i in range(len(input)):  # O(n)
#         i = 0
#         anotherFunction()  # O(n)
#         stranger = True  # O(n)
#         a += 1  # O(n)
#         i += 1
#     return a  # O(1)


# funChallenge()
# # O(3 + 4n)  O(n)

#######################################################################
def anotherfunchallenge(input):
    a = 5  # O(1)
    b = 10  # O(1)
    c = 50  # O(1)
    for i in range(input):
        i = 0
        x = i + 1  # O(n)
        y = i + 2  # O(n)
        z = i + 3  # O(n)
        i += 1
    for j in range(input):
        j = 0
        p = j * 2  # O(n)
        q = j * 2  # O(n)
        j += 1
    whoAmI = "I don't know"  # O(1)


# O(4 + 5n) O(n)
