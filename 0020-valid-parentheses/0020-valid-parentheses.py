class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        valid={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for i in range(len(s)):
            if s[i] in valid.values():
                a.append(s[i])
            else:
                if not a:
                    return False
                last=a.pop()
                if s[i] in valid and last!=valid[s[i]]:
                    return False
        return len(a)==0