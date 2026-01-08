class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a=[]
        exp=['+','-','*','/']
        for token in tokens:
            if token not in exp:
                a.append(int(token))
            else:
                if token =='+':
                    a.append(a.pop()+a.pop())
                elif token =='-':
                    a.append((a.pop()-a.pop())*-1)
                elif token =='*':
                    a.append(a.pop()*a.pop())
                else:
                    first=a.pop()
                    second=a.pop()
                    got=int(second/first)
                    print('Got by Division: ', got)
                    a.append(got)
        return a[-1]
        