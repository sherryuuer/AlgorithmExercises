array = [5, 9, 3, 10, 45, 2, 0]
# array.insert(1, 4)
# print(array)


def my_insertion_sort(arr):
    result_arr = [arr[0], ]
    for n in arr[1:]:
        is_over = False
        for i in range(len(result_arr)):
            if n < result_arr[i]:
                result_arr.insert(i, n)
                is_over = True  # give it a signal to tell if it need a append
                break  # get out of the check insert loop
        if is_over is False:  # if got the not haven insert signal, append
            result_arr.append(n)
        print(result_arr)
    return result_arr


def g_insertion_sort(arr):
    result_arr = [arr[0]]
    for n in arr[1:]:
        insert_index = 0
        # this loop will find the index to insert into.
        for i in range(len(result_arr)):
            if n < result_arr[i]:
                insert_index = i
                break
            insert_index = i + 1
        # insert
        result_arr = result_arr[:insert_index] + [n] + result_arr[insert_index:]
    print(result_arr)
    return result_arr


g_insertion_sort(array)
