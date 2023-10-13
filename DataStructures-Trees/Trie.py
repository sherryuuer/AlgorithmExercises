class TrieNode:
    def __init__(self):
        # every node has a dict to store children，key is char，values are children nodes.
        self.children = {}
        # mark if a word is over
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        # init root node
        self.root = TrieNode()

    def insert(self, word):
        # insert char from root node
        node = self.root
        for char in word:
            if char not in node.children:
                # if the char is not exsit, create a new node.
                node.children[char] = TrieNode()
            node = node.children[char]
        # mark the last node of the word as end of the word.
        node.is_end_of_word = True

    def search(self, word):
        # search from root node
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word  # return if u found the entire word.

    def startsWith(self, prefix):
        # search the prefix from root node
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True  # found it no matter if it is entire word.


trie = Trie()
# insert
trie.insert("apple")
trie.insert("app")

print(trie.search("apple"))  # True
print(trie.search("app"))    # True
print(trie.search("appl"))   # False

print(trie.startsWith("appl"))  # True
print(trie.startsWith("ban"))   # False
