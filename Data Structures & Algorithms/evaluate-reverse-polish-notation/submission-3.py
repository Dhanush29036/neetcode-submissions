class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for i in tokens:
            if i=="+":
                a=int(s.pop())
                b=int(s.pop())
                s.append(a+b)
            elif i=="-":
                a=int(s.pop())
                b=int(s.pop())
                s.append(b-a)
            elif i=="/":
                a=int(s.pop())
                b=int(s.pop())
                s.append(b/a)
            elif i=="*":
                a=int(s.pop())
                b=int(s.pop())
                s.append(b*a)
            else:
                s.append(int(i))
        return int(s[0])

    
