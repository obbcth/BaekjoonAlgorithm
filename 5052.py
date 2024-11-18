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


t = int(input())
for _ in range(t):
    n = int(input())
    trie = Trie()

    arr = []

    for __ in range(n):
        query = input().strip()
        trie.insert(query)
        arr.append(query)

    valid = True

    for i in arr:
        res = trie.search_prefix(i)
        if res != None and len(res.children) != 0:
            valid = False
            break

    if valid:
        print("YES")
    else:
        print("NO")