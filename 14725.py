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

for _ in range(t):
    
    query = input().strip().split(" ")
    query = query[1:]
    trie.insert(query)


def dfs(trie, depth):
    if len(trie.children) != 0:
        child_list = list(trie.children.keys())
        child_list.sort()
        
        for child in child_list:
            print("--"*depth + child)
            dfs(trie.children[child], depth+1)

dfs(trie, 0)