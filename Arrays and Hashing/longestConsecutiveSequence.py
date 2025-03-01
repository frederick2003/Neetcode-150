"""
128. Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3

"""
def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # The first thing you have to do it find the start of the sequence
    # for any value in nums, it is a start of a CS if value-1 is not in nums

    # Convert the list to a set
    # O(n)
    number_set = set(nums)
    # Now find the beginings of all CS's
    start = []
    # O(n)
    for num in number_set:
        # O(1)
        if num - 1 not in number_set:
            # O(1)
            start.append(num)
    
    # How do i iterate over all the possible sequences?
    if len(start) == 0:
        return 0
    i = 0
    maximum = 1
    while i < len(start):
        current_max = 1
        current = start[i]
        while current + 1 in number_set:
            current+= 1
            current_max+=1
        maximum = max(current_max, maximum)
        i+=1
    return maximum
