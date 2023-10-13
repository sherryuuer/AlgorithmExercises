string = "I am a word called mikky."
# string = "abc"
# print(string[0])


def reverse_normal(string):
    char_list = []
    string_list = list(string)
    print(string_list)
    if len(string_list) < 2:
        return string
    else:
        for i in range(len(string_list)):
            char_list.append(string_list.pop())
            print(char_list)
        reversed_string = "".join(x for x in char_list)
        return reversed_string


def reverse_recursion(string):
    length = len(string)
    if length < 1:
        return string
    last_char = string[length - 1]
    print(last_char, end="")
    return reverse_recursion(string[:length - 1])


# another way- tail recursion
def reverse_string(s):
    print(s)
    if len(s) <= 1:
        return s
    else:
        first_char = s[0]
        rest_of_string = s[1:]
        reversed_rest = reverse_string(rest_of_string)
        return reversed_rest + first_char


reversed_string = reverse_string(string)
print(reversed_string)

# cool!
# I am a word called mikky.
#  am a word called mikky.
# am a word called mikky.
# m a word called mikky.
#  a word called mikky.
# a word called mikky.
#  word called mikky.
# word called mikky.
# ord called mikky.
# rd called mikky.
# d called mikky.
#  called mikky.
# called mikky.
# alled mikky.
# lled mikky.
# led mikky.
# ed mikky.
# d mikky.
#  mikky.
# mikky.
# ikky.
# kky.
# ky.
# y.
# .
# .ykkim dellac drow a ma I
