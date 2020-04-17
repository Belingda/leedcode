# https://leetcode-cn.com/problems/merge-sorted-array/
class Solution:
	def merge(self, nums1, m: int, nums2, n) -> None:
		"""
		Do not return anything, modify nums1 in-place instead.
		"""
		i1 = 0
		i2 = 0
		while (i2 < len(nums2)):
			if nums2[i2] < nums1[i1]:
				nums1[i1] = nums2[i2]
				i2 += 1
			i1 +=1


