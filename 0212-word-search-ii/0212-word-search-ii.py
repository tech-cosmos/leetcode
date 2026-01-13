class TrieNode:
    def __init__(self):
        self.children={}
        self.word=None

    def insert(self,word):
        node=self
        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]
        node.word=word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m=len(board)
        n=len(board[0])
        res=[]

        root=TrieNode()

        for w in words:
            root.insert(w)
        
        def dfs(r,c,node):
            ch=board[r][c]

            if ch not in node.children:
                return
            
            nxt=node.children[ch]

            if nxt.word is not None:
                res.append(nxt.word)
                nxt.word=None
            
            board[r][c]="#"

            if r>0 and board[r-1][c]!="#":
                dfs(r-1,c,nxt)
            if r+1<m and board[r+1][c]!="#":
                dfs(r+1,c,nxt)
            if c>0 and board[r][c-1]!="#":
                dfs(r,c-1,nxt)
            if c+1<n and board[r][c+1]!="#":
                dfs(r,c+1,nxt)
            
            board[r][c]=ch

        for i in range(m):
            for j in range(n):
                dfs(i,j,root)
        
        return res
