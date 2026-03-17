"""
PROBLEM: 3SUM

Statement:
Given an integer array 'nums', return all unique triplets [nums[i], nums[j], nums[k]] 
such that:
1. i != j, i != k, and j != k (distinct indices)
2. nums[i] + nums[j] + nums[k] == 0

Constraints:
- 3 <= nums.length <= 500
- -10^3 <= nums[i] <= 10^3

Technique: Sorting + Two Pointers
Time Complexity: O(N^2)
Space Complexity: O(1) or O(N) depending on sorting implementation
"""


def three_sum(nums):
    ans = []
    nums.sort()
    n = len(nums)
    
    for i in range(0,n):
        
        if (i == 0 or nums[i] != nums[i-1]):
            lpt = i + 1
            rpt = n - 1
            
            while lpt < rpt:
                sum = nums[i] + nums[lpt] + nums[rpt]
                if sum < 0:
                    lpt += 1
                elif sum > 0:
                    rpt -= 1
                else:
                    ans.append([nums[i],nums[lpt],nums[rpt]])
                    lpt += 1
                    rpt -= 1
                    while (lpt < rpt and nums[lpt] == nums[lpt-1]):
                        lpt += 1
                    while(lpt < rpt and nums[rpt] == nums[rpt + 1]):
                        rpt -= 1
    
    return ans
