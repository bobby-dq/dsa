# Statement

# Given an integer array, nums, find and return all unique triplets [nums[i], nums[j], nums[k]], such that i ≠= j, i ≠= k, and j ≠= k and nums[i] + nums[j] + nums[k] ==0==0.

#      Note: The order of the triplets in the output does not matter.

#  Constraints:

#      3 ≤ 3 ≤ nums.length ≤500≤500

#      −10^3≤−10^3≤ nums[i] ≤103≤103

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
