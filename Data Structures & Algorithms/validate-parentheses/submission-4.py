class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<2:
            return False
        st=[]
        a="[{("
        for i in s:
            print(st)
            if i in a:
                st.append(i)
            elif not st:
                return False
            elif i==')':
                if st[-1]=='(':
                    st.pop()
                else:
                    return False
            elif i=='}':
                if st[-1]=='{':
                    st.pop()
                else:
                    return False
            elif i==']':
                if st[-1]=='[':
                    st.pop()
                else:
                    return False
        if not st:
            return True
        return False