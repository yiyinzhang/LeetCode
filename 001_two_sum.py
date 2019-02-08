'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

'''
Solution 1
'''

class Solution1(object):
	def twoSum(self, nums, target):
		for i in range(len(nums)):
			for j in range(i+1, len(nums)):
				if nums[i] + num[j] == target:
					return [i, j]

'''
Solution 2
'''

class Solution2(object):
	def twoSum(self, nums, target):
		lookup = {}
		for i, num in enumerate(nums):
			if target - num in lookup:
				return [lookup[target - num], i]
			else:
				lookup[num] = i