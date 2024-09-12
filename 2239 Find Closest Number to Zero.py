"""

2239. Find Closest Number to Zero
Solved
Easy
Topics
Companies
Hint
Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

 

Example 1:

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
Example 2:

Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
 

Constraints:

1 <= n <= 1000
-105 <= nums[i] <= 105
"""


nums = [-4,-2,1,4,8]

Output = abs(nums[0]) # =4

for i in range(0 ,len(nums)-1):

    if abs(nums[i+1]) < abs(Output):
        Output = abs(nums[i+1])
        result = nums[i+1]
    elif abs(nums[i+1]) == Output & nums[i+1] > nums[i]:
        result = nums[i+1]

print(result)
  

