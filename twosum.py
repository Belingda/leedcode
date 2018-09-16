class Solution(object):
    def twoSum(self,nums,target):
        temp={}
        for index1,num in enumerate(nums):
            index2=temp.get(target-num)
            if index2!=None:
               return [index2,index1]
            else:
                temp[num]=index1
ob=Solution()
nums=[2,7,8,1]
target=9
result=ob.twoSum(nums,target)
print result

