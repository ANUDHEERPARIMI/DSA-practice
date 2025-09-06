class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        n=len(order)
        m=len(friends)
        d={}
        def binarys(target):
            low=0
            high=m-1
            while low<=high:
                mid=(low+high)//2
                if friends[mid]==target:
                    return mid
                elif friends[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return -1
        for i in range(n):
            idx=binarys(order[i])
            if idx!=-1:
                d[i]=friends[idx]
        return list(d.values())

        