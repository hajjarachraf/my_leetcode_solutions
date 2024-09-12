"""217. Contains Duplicate
Easy
Topics
Companies
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true"""


"""solution 1 with no set"""
# nums = [1,1,1,3,3,4,3,2,4,2]

# nums.sort()

# for i in range(len(nums)-1):
#     if nums[i] == nums[i+1]:
#         print(True)  # print(True)=>return True
# print(False) # print(False)=>return False
"""solution 2 with set"""

nums = [1,1,1,3,3,4,3,2,4,2]
nums_set = set(nums)

if len(nums) == len(nums_set):
    print(False)
else:
    print(True)
 
            
