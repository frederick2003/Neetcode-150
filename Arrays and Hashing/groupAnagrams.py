"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""

def groupAnagrams(self, strs):
    defaultdict = defaultdict(list)
    if len(strs) == 1:
        return [[strs[0]]]
    
    ana_map = defaultdict(list)
    for i, string in enumerate(strs):
        sorted_str = ''.join(sorted(string))
        ana_map[sorted_str].append(string)
    
    return ana_map.values()