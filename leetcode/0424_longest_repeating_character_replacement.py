# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/
# Medium
# O(n) time, O(1) space, where n is the length of the string and the space is O(1) because there are only 128 ASCII characters
# Sliding Window
# Similar to 3. Longest Substring Without Repeating Characters, but instead of checking if the character is in the window, 
# we check if the number of characters that need to be replaced is greater than k. We keep track of the frequency of each 
# character in the window and the maximum frequency of any character in the window. If the number of characters that need to
# be replaced (window size - max frequency) is greater than k, we shrink the window from the left until it is valid again. 
# We update the longest length at each step.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        longest = 0
        left = 0
        max_freq = 0
        freq = {}

        for right in range(len(s)):
            freq[s[right]] = 1 + freq.get(s[right], 0)
            max_freq = max(max_freq, freq[s[right]])

            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
        
        return longest