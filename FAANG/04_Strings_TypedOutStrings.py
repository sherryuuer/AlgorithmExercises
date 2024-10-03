# what is this mean?
# Give 2 String S and T, are they equal??
# if there is a #, it means backspace(delete the character)

# Constraints
# Will the # at the beginning? delete nothing
# When nothing to delete, it will just delete noting!
# All the character is lower case? case sensitive? yes, A is not equal to a
# When 2 # appear? delete 2 characters before the first #
# Are 2 empty string equal to each other? yes


# Brute force logic
# the space complex may got big
# Time/Space : O(m + n), and the Space is the part can be optimized
class Solution1(object):
    def typedOutStringEquals(self, S, T):

        def _typeString(string):
            s = []

            if not string:
                return ""

            for c in string:
                if c != "#":
                    s.append(c)
                elif c == "#" and len(s) > 0:
                    s.pop()

            return "".join(s)

        typedS = _typeString(S)
        typedT = _typeString(T)

        if len(typedS) != len(typedT):
            return False

        for i in range(len(typedS)):
            if typedS[i] != typedT[i]:
                return False

        return True


s1 = Solution1()


class Solution2(object):
    def typedOutStringEquals(self, S, T):
        sPointer = len(S) - 1
        tPointer = len(T) - 1

        def _findValid(string, pointer, count=0):
            while pointer >= 0:
                if string[pointer] == "#":
                    count += 1
                    pointer -= 1
                # if char but count is not 0, skip the char
                elif count != 0:
                    count -= 1
                    pointer -= 1
                else:
                    break
            return pointer

        # here is tricky!! or make the process complete, but we need to compare more
        while sPointer >= 0 or tPointer >= 0:
            # try to find the first not # char
            # if # count up
            sPointer = _findValid(S, sPointer)
            tPointer = _findValid(T, tPointer)

            # compare the 2 char!! notice the and and or!! for the last test case!
            if sPointer >= 0 and tPointer >= 0:
                if S[sPointer] != T[tPointer]:
                    return False
            elif sPointer >= 0 or tPointer >= 0:
                return False

            sPointer -= 1
            tPointer -= 1

        return True


s2 = Solution2()


testcases = [
    [["ab#c", "ac"], True],
    [["ab#c", "acc#"], True],
    [["ab#c", "acc#d"], False],
    [["ab##", "ab"], False],
    [["bxj##tw", "bxo#j##tw"], True],
    [["bbbextm", "bbb#extm"], False],
]

for i, testcase in enumerate(testcases):
    strings = testcase[0]
    result = testcase[1]

    S, T = strings[0], strings[1]
    if s2.typedOutStringEquals(S, T) == result:
        print(f"pass case {i}")
    else:
        print(f"failed with case {i}: {testcase}")
