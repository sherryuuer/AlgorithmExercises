s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]


res = []
map = {}
for index in range(len(s)-9):
    substr = s[index:index+10]
    if substr not in map:
        map[substr] = 1
    else:
        map[substr] += 1
        if map[substr] == 2:
            res.append(substr)

print(res)
