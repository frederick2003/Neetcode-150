"""
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

def isAnagram(self, s, t):
    s_map = {}
    for letters in s:
        if letters not in s_map:
            s_map[letters] = 1
        else:
            s_map[letters] +=1

    t_map = {}
    for letters in t:
        if letters not in t_map:
            t_map[letters] = 1
        else:
            t_map[letters] +=1
    return t_map==s_map