from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        b=[[] for i in range(len(nums)+1)]
        for num,freq in count.items():
            b[freq].append(num)
        ans = []
        for i in range(len(b)-1,0,-1):
            for j in b[i]:
                ans.append(j)
            if k == len(ans):
                return ans


        