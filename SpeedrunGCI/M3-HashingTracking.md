## HashMap
1. Data access
2. Pair-wise relation

- **Logger Rate Limiter**
```python
# time O(1), space O(n)
class RequestLogger:
    def __init__(self, time_limit):
        self.logger_map = {}
        self.time_limit = time_limit

    def message_request_decision(self, timestamp, request):
        # if request not in self.logger_map:
        #     self.logger_map[request] = timestamp
        #     return True

        # else:
        #     time_interval = timestamp - self.logger_map.get(request)
        #     if time_interval >= self.time_limit:
        #         self.logger_map[request] = timestamp
        #         return True
        #     else:
        #         return False
        # can be improve!
        if request not in self.logger_map or timestamp - self.logger_map.get(request) >= self.time_limit:
            self.logger_map[request] = timestamp
            return True
        else:
            return False
```

## Knowing What to Track
1. Counting element/Frequency tracking: 但是实际上array用index作为count的key也是很有效率的
2. Pattern recognition
3. Fixed set of possibilities

- **Longest Palindrome by Concatenating Two-Letter Words**
```python
words1 = [“ab”, “cd”, “ef”, “gh”, “ij”] # 0 distinct = 5, same = 0
words2 = [“aa”, “bb”, “cc”, “dd”, “ee”] # 2 distinct = 0, same = 5
words3 = [“aa”, “bb”, “aa”, “ea”] # 6 distinct = 1, same = 3
words4 = [“aa”, “bb”, “aa”, “bb”, “aa”, “bb”] # 10 distinct = 0, same = 7

# X use a hashmap1 to track the number of the res -> calculate the length
# use a hashmap2 to track the number in storage
# X use a odd_exist = False, odd_word = ""
#
# ab -> not exsit in res: add to storage
#    -> reverse exsit in storage: remove 1 of the reverse
# aa -> exsit in res: 1, and odd_word = aa, then add to res and clear the odd
#                     2, and odd_word != aa, add to res and set the odd
#    -> not exsit in res: and odd_word = "" add to res and set the odd

def longest_palindrome(words):
    from collections import defaultdict
    storage_map = defaultdict(int)
    length = 0

    for word in words:
        if word[0] != word[1]:
            reverse_word = word[1] + word[0]
            if storage_map[reverse_word] > 0:
                length += 4
                storage_map[reverse_word] -= 1
            else:
                storage_map[word] += 1

        else:
            if storage_map[word] > 0:
                length += 4
                storage_map[word] -= 1

            else:
                storage_map[word] += 1

    for word in storage_map:
        if storage_map[word] > 0 and word[0] == word[1]:
            length += 2
            break

    return length

# handy test
word = ["aa", "bb", "cc", "dd"]
storage = {"bb": 1, }
res = {"aa": 1, }
odd = "aa"
```
- 按照思考的路径找到答案。直觉也是一种找到答案的好方法。
- 这道题，解答给出的方法很聪明，尝试写一下：
```python
def longest_palindrome(words):
    from collections import Counter
    word_map = Counter(words) # Space O(26^2)/O(n) time O(n)
    odd_word = False
    result = 0

    for word, count in word_map.items():
        if word[0] == word[1]:
            if count % 2 == 0:
                result += count * 2
            else:
                result += (count - 1) * 2
                odd_word = True
        elif word[1] > word[0]: # ensure calculate once
            result += min(count, word_map.get(word[1] + word[0], 0)) * 4

    return result + 2 if odd_word else result
# 注意，Counter会给任何一个不存在的元素一个 0 count
```
