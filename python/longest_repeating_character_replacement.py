"""
PROBLEM: LONGEST REPEATING CHARACTER REPLACEMENT

Statement:
Given a string 's' and an integer 'k', find the length of the longest substring 
containing the same letter after replacing at most 'k' characters with any 
other uppercase English character.

Constraints:
- 1 <= s.length <= 10^3
- s consists of uppercase English characters.
- 0 <= k <= s.length

Technique: Sliding Window (Dynamic)
Time Complexity: O(N) - We traverse the string once.
Space Complexity: O(26) or O(1) - The frequency map only stores 26 uppercase letters.
"""