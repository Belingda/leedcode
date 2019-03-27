
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums and len(nums)==0:
            return 0
        d={}
        for num in nums:
            d[num]=d.get(num,0)+1
        max,maxcnt=0,0
        for num,cnt in d.items():
            if cnt>maxcnt:
                maxcnt=cnt
                max=num
        return max   
# 摩尔投票法

class Solution(object):
    def majorityElement(self, nums):
        target, cnt = 0, 0
        for num in nums:
            if num == target:
                cnt += 1
            elif cnt == 0:
                target, cnt = num, 1
            else:
                cnt-=1
        return target