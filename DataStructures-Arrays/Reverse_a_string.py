# My solution
def reverse(str):
    reverse_str = []
    for i in range(len(str)):
        reverse_str.append(str[-1])
        str = str[:-1]
    return "".join(reverse_str)


print(reverse("helloworld"))


# Answer
def reverse(stri):
    mylist = []
    for i in range(len(stri) - 1, -1, -1):  # 9, -1, -1
        mylist.append(stri[i])
    return ''.join(mylist)

x = reverse('I am theja')
print(x)
# or just stri[::-1]
