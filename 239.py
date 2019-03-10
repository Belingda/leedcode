# some tips:windows滑动窗户 可以只记下标 解决不知道pop哪个的问题 
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        self.windows=[]
        self.results=[]
        for i in range(len(nums)):
            if i>=k and i-self.windows[0]>=k:
                self.windows.pop(0) # 前面一个
            while len(self.windows)>0 and nums[self.windows[-1]]<nums[i]:
                    self.windows.pop() # 保证窗口最前面一个数是最大值
            self.windows.append(i)
            if i>=   k-1:
                self.results.append(nums[self.windows[0]])
        return self.results

ob=Solution()                  
print(ob.maxSlidingWindow([7,2,4],2))          
                