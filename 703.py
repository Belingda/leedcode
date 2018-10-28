from heapq import *
class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums=[]
        self.k=k
        for num in nums:
            heappush(self.nums,num)
        size=len(self.nums)
        while size>k:
            size-=1
            heappop(self.nums)
        
        print self.nums

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if val<self.nums[0]:
            return self.nums[0]
        else:
            heapreplace(self.nums,val)
            return self.nums[0]
           

ob=KthLargest(3,[9,8,7,1,2,3,])
print ob.add(0)
print ob.add(9)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)