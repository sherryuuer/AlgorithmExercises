basket = [1, 5, 5, 3, 90, 56, 34, 23]


def my_bubble_sort(basket):
    while True:
        count = 0
        for i in range(len(basket) - 1):
            if basket[i] > basket[i + 1]:
                tmp = basket[i]
                basket[i] = basket[i + 1]
                basket[i + 1] = tmp
                count += 1
        if count == 0:
            break
    return basket

# basket = my_bubble_sort(basket)
# print(basket)


def bubble_sort(basket):
    n = len(basket)
    while True:
        swapped = False
        for i in range(n - 1):
            if basket[i] > basket[i + 1]:
                basket[i], basket[i + 1] = basket[i + 1], basket[i]  # Swap elements
                swapped = True
        if not swapped:
            break
    return basket


# sorted_basket = bubble_sort(basket)
# print(sorted_basket)


# Because every round, the biggest number will always goto the end.
# so this how it comes this
def bubble_sort_ztm(array):  # O(n^2)
    count = 0
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            # In every iteration of the outer loop, one number gets sorted. So the inner loop will run only for the unsorted part
            # print(j)
            count += 1
            if array[j] > array[j + 1]:
                # print((array[j], array[j + 1]))
                array[j], array[j + 1] = array[j + 1], array[j]
            # print(array)
        # print("---")
    return (f'{array} \nNumber of comparisons = {count}')
# 两层嵌套，每一次都把最大的拿到了右边
# 另一种方式也是同理，就是从最右边开始，每一轮都把最小的移动到左边


# run it and see the numbers.
array = [5, 9, 3, 10, 45, 2, 0]
bubble_sort_ztm(array)
