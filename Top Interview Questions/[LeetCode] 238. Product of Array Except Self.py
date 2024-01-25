# https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-interview-150
'''

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prrefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        N = len(nums)
        answer = [1 for _ in range(N)]
        for i in range(1, N):
            answer[i] = answer[i-1] * nums[i-1]
        # print(answer) # left -> right
        temp = 1
        # right -> left
        for i in range(N-2, -1, -1):
            temp *= nums[i+1]
            answer[i] *= temp

        return answer

# Test Case 
s = Solution()
answer = s.productExceptSelf(nums=[1,2,3,4])
print(answer)