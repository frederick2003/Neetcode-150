"""
238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

def productExceptSelf(self, nums):
    if len(nums) == 2:
        return [nums[1], nums[0]]
    result = [0 for i in range(len(nums))]
    result[0] = 1
    current = nums[0]
    for i in range(1, len(nums)):
        result[i] = current
        current*=nums[i]
    current = nums[-1]
    for i in range(len(nums)-2, -1,-1):
        result[i] *= current
        current*=nums[i]
    return result