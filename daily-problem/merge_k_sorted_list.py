# return a new sorted merged list from K sorted lists, each with size N.
import heapq
lists = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
# the result should be [10, 12, 15, 15, 17, 20, 20, 30, 32]
# steps:
# 将每个list的第一个元素放进heap，（element， list的index，element的index）
# 直到heap为空，不断弹出和送入元素


def merge(lists):
    result = []

    min_heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(min_heap)

    while min_heap:
        val, lst_index, val_index = heapq.heappop(min_heap)
        result.append(val)

        if val_index < len(lists[lst_index]) - 1:
            insert_val = lists[lst_index][val_index + 1]
            heapq.heappush(min_heap, (insert_val, lst_index, val_index + 1))

    return result


print(merge(lists))
