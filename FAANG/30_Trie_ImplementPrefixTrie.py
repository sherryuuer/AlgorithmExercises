# Constraints:
# Can we use helper function? yes
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.word

    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


trie = Trie()
trie.insert("apple")
print(trie.search("dog"))  # False
trie.insert("dog")
print(trie.search("dog"))  # True
print(trie.startsWith("app"))  # True
print(trie.search("app"))  # False
trie.insert("app")
print(trie.search("app"))  # True
