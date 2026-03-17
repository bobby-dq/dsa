"""
PROBLEM: REPEATED DNA SEQUENCES

Statement:
A DNA sequence consists of nucleotides represented by 'A', 'C', 'G', and 'T'. 
Given a string 's', return all the 10-letter-long sequences (continuous substrings 
of exactly 10 characters) that appear more than once in s. 

Constraints:
- 1 <= s.length <= 10^3
- s[i] is either 'A', 'C', 'G', or 'T'.

Technique: Sliding Window + Hash Set
Time Complexity: O(N) 
Space Complexity: O(N)
"""

def findRepeatedDnaSequences(s):
    seen = []
    repeating = []
    n = len(s)
    lptr = 0
    rptr = 10
    
    while(rptr < n):
        sub_str = s[lptr:rptr]
        
        if ((sub_str in seen) and (sub_str not in repeating)):
            repeating.append(sub_str)
        else:
            seen.append(sub_str)
        lptr += 1
        rptr += 1
    
    
    # Replace this placeholder return statement with your code 
    return repeating