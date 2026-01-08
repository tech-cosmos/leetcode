class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        valid_open=['(','{','[']
        for i in range(len(s)):
            if s[i] in valid_open:
                a.append(s[i])
            else:
                if not a:
                    return False
                last=a.pop()
                if s[i]==')' and last!='(':
                    return False
                elif s[i]==']' and last!='[':
                    return False
                elif s[i]=='}' and last!='{':
                    return False
        return len(a)==0