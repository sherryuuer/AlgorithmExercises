# Google Question
# Given an array, return the first recurring character
# Example1 : array = [2,1,4,2,6,5,1,4]
# It should return 2
# Example 2 : array = [2,6,4,6,1,3,8,1,2]
# It should return 6

# Mine is not right! check it.
def hashtable(list):
    myhash = {}
    for i in set(list):
        # {element: [times, first_position]}
        # find times > 1 and min(first_position) then get the ele.
        myhash[i] = [list.count(i), list.index(i)]
    myhash = {key: value[1] for key, value in myhash.items() if value[0] > 1}
    min_key = min(myhash, key=lambda k: myhash[k])
    return min_key


# This is not right too,check it !
def func(mylist):
    for i in range(0, len(mylist)):
        for j in range(i + 1, len(mylist)):
            if mylist[i] == mylist[j]:
                return mylist[i] 
    return 0


# normal answer but not right!
def func_normal(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                return list[i]
    return None


# normal answer but right? Good, I made it!
def func_normal_r(list):
    mylist = []
    for i in list:
        if i in mylist:
            return i
        mylist.append(i)
    return None


def hashtable_2(mylist):
    mydict = {}
    for i in range(0, len(mylist)):
        if mylist[i] in mydict:
            return mylist[i]
        else:
            mydict[mylist[i]] = i
    return 0


# This one just like hashtable_2, but hashtable is good for searching speed.
def simple_frc(array):
    dictionary = dict()
    for item in array:
        if item in dictionary:
            return item
        else:
            dictionary[item] = True
    return None


mylist = [2, 1, 1, 2, 3, 4, 5]
x = func_normal_r(mylist)
print(x)
