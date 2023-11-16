from collections import deque


graph = {}
# this can be a graph, with node and line
graph["me"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
# 以上编写的顺序并不重要，因为散列表是无序的


def person_is_jonny(check_person):
    return check_person == "jonny"


def find_person():
    # 创建一个空的双端队列
    my_deque = deque()
    my_deque += graph["me"]
    inqueue_list = set()
    while my_deque:
        print(my_deque)
        check_person = my_deque.popleft()
        if person_is_jonny(check_person):
            return "found"
        else:
            my_deque += [p for p in graph[check_person] if p not in inqueue_list]
        inqueue_list.add(check_person)
        print(f"checked: {inqueue_list} -------------")
    return "not found"


# result = find_person()
# print(result)


# book's good way
def search_person():
    # 创建一个空的双端队列
    my_deque = deque()
    my_deque += graph["me"]
    checked = set()
    while my_deque:
        print(my_deque)
        check_person = my_deque.popleft()
        if check_person not in checked:
            if person_is_jonny(check_person):
                return "found"
            else:
                my_deque += graph[check_person]
                checked.add(check_person)
    return "not found"


result = search_person()
print(result)

# 以上问题来自算法图解的广度优先搜索章节






# my_deque.append(1)
# my_deque.appendleft(0)
# removed_element = my_deque.pop()
# removed_element_left = my_deque.popleft()

