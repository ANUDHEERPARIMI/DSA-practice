from collections import defaultdict
from typing import List
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        map1=defaultdict(int)
        for num in nums:
            map1[num]+=1
        n=len(nums)
        if n%k!=0:
            return False
        m=len(map1.keys())
        for i in range(n):
            if map1[nums[i]]>n//k:
                return False
        return True
        