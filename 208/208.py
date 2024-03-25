class Trie:

    def __init__(self):
        self.children = {}
        self.ends = False

    def insert(self, word: str) -> None:
        p = self
        for c in word:
            if c not in p.children:
                p.children[c] = Trie()
            p = p.children[c]
        p.ends = True


    def search(self, word: str) -> bool:
        p = self
        for c in word:
            if c not in p.children:
                return False
            p = p.children[c]
        return p.ends

    def startsWith(self, prefix: str) -> bool:
        p = self
        for c in prefix:
            if c not in p.children:
                return False
            p = p.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
