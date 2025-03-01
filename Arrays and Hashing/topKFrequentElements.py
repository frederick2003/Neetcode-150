"""
347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

def topKFrequent(self, nums, k):
    # The idea is to have an array that uses the indices of the array as the frequency.
    # map the elements that occur that many times to the corresponding index.
    # Then travers the output array form 1 <= max and return the k most frequent elements.

    #   TC : O(n+1)
    freq_list = [[]] * (len(nums) + 1)

    #   TC : O(n)
    freq_map = {}
    for number in nums:
        if number not in freq_map:
            freq_map[number] = 1
        else:
            freq_map[number] += 1

    # Now append all elements to the bucket array at where (index = their frequency in the input array)
    # TC:   O(len(freq_map))
    for key, value in freq_map.items():
        freq_list[value] = freq_list[value] + [key]
    
    result = []
    # Travers the freq array and return the k most elements
    for i in range(len(freq_list)-1, 0,-1):   
        if freq_list[i] != []:
            for j in range(len(freq_list[i])):
                result.append(freq_list[i][j])
                k-=1
                if k == 0:
                    return result