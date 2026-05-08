# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Medium
# O(n) time, O(1) space, where n is the length of the string and the space is O(1) because there are only 128 ASCII characters
# Sliding Window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            
            while s[right] in window:
                window[s[left]] = window[s[left]] - 1
                if window[s[left]] == 0:
                    del window[s[left]]
                
                left += 1

            window[s[right]] = window.get(s[right], 0) + 1

            longest = max(longest, right - left + 1)
        
        return longest