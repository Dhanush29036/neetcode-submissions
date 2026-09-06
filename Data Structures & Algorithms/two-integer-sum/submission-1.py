class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=defaultdict(int)
        c=0
        for i in nums:
            if d[target-i]!=0:
                return [d[target-i]-1,c]
            d[i]=c+1
            c+=1
        return [0,0]