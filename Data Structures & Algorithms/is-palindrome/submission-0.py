class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(list(s.split()))
        s=s.lower()
        t=""
        for i in s:
            if i.isalnum():
                t+=i
        return t==t[::-1]