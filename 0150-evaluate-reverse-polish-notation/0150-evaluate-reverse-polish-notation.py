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
                    denominator=a.pop()
                    numerator=a.pop()
                    a.append(int(numerator/denominator))
        return a[-1]
        