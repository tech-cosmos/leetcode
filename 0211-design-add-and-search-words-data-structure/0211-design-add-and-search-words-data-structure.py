class WordDictionary:

    def __init__(self):
        self.children={}
        self.is_end=False        

    def addWord(self, word: str) -> None:
        node=self
        for ch in word:
            if ch not in node.children:
                node.children[ch]=WordDictionary()
            node=node.children[ch]
        node.is_end=True

    def search(self, word: str) -> bool:
        node=self
        for i,ch in enumerate(word):
            if ch == '.':
                found=False
                for val in node.children.keys():
                    child=node.children[val]
                    if child.search(word[i+1:]):
                        found=True
                        break
                return found
            elif ch not in node.children:
                return False
            else:
                node=node.children[ch]
        return node.is_end


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)