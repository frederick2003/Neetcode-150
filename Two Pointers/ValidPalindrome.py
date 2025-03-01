"""
125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""
def isPalindrome(s):
    # Case 1: String is of even length
    # Case 2: String is of odd length
    if len(s) == 1:
        return True
    left = 0
    right = len(s)-1
    while left < right:
        if s[left].isalnum() and s[right].isalnum():
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
        else:
            if not s[left].isalnum():
                left+=1
            elif not s[right].isalnum():
                right-=1
    return True