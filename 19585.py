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

c, n = map(int, input().split())
trie = Trie()
nick = set() 

for _ in range(c):
    trie.insert(input().strip())

for _ in range(n):
    nick.add(input().strip())

q = int(input())
for _ in range(q):
    query = input().strip()
    
    node = trie
    valid = False
    for i in range(len(query)):
        char = query[i]
        if char in node.children:
            node = node.children[char]
            if node.is_end and query[i+1:] in nick:
                valid = True
                break
        else:
            break

    if valid:
        print("Yes")
    else:
        print("No")