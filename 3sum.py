class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
       """
        rets=set()
        nums=sorted(nums)
        print(nums)
        for j in range(len(nums)):
            for i in range(j+1,len(nums)):
                temp=-(nums[j]+nums[i])
                if temp in nums:
                    rets.add((nums[j],nums[i],temp))
        print(rets)
        return rets

ob=Solution()
ob.threeSum([-1, 0, 1, 2, -1, -4])
