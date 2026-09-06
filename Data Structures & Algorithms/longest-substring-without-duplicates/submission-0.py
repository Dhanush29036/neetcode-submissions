class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        n=len(s)
        m=0
        d=defaultdict(int)
        while i<n and j<n:
            d[s[i]]+=1
            while d[s[i]]>1:
                d[s[j]]-=1
                j+=1
            m=max((i-j+1),m)
            i+=1
        return m
    
            