class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        subset=[]

        def dfs(i):
            if i>=len(digits):
                res.append("".join(subset))
                return
            digit=digits[i]
            for c in digitToChar[digit]:
                subset.append(c)
                dfs(i+1)
                subset.pop()
            
        dfs(0)
        return res
        