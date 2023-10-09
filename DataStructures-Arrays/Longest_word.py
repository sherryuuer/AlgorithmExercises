def LongestWord(sen):
    import re
    cleaned_str = re.sub(r'[^a-zA-Z\s]', ' ', sen)
    word_list = cleaned_str.split()
    max_length_element = max(word_list, key=len)
    return max_length_element
# re 模块是 Python 中的正则表达式模块，用于处理文本匹配和替换等操作。

# re.sub() 函数用于替换字符串中匹配正则表达式的部分。

# 在这里，正则表达式模式 r'[^a-zA-Z\s]' 用于匹配除了字母和空白字符以外的任何字符。

# ' ' 是替换后的内容，即用空格字符替换匹配到的字符。

# sen 是输入的字符串，这是被替换的目标字符串。


# keep this function call here
print(LongestWord("I love shiogn%jfin"))


# 当使用 max 函数时，可以使用 key 参数
# 来指定一个函数，该函数将应用于可迭代对象中的每个元素，并根据函数的返回值来确定最大的元素。这种技巧非常有用，因为它允许你在比较元素时考虑元素的某些特性而不仅仅是它们的值。

# 在上面的示例中，我们有一个列表 my_list 包含了一些字符串，我们想找到其中最长的字符串。为了实现这个目标，我们使用了 key=len 参数。这个参数告诉 max 函数在比较元素时，使用每个元素的长度来进行比较。

# 具体步骤如下：

# max 函数遍历 my_list 中的每个元素。
# 对于每个元素，它应用了 len 函数，计算元素的长度。
# 然后，它将每个元素的长度用作比较的标准。
# 最后，它返回具有最大长度的元素。

# 常规做法
# my_list = ["apple", "banana", "cherry", "date", "elderberry"]

# max_length = 0  # 用于存储最大长度的初始值
# longest_word = ""  # 用于存储最长单词的初始值

# for word in my_list:
#     if len(word) > max_length:
#         max_length = len(word)
#         longest_word = word

# print("最长的单词是:", longest_word)
