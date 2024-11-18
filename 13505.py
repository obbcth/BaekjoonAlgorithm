import sys
input = sys.stdin.readline

class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.is_end = True

    def search_prefix(self, word):
        node = self
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node


trie = Trie()
t = int(input())

arr = list(map(int, input().split()))

for i in arr:
    trie.insert('{:032b}'.format(i))
