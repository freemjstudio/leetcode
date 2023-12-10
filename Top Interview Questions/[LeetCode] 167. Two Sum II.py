# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        answer = [-1, -1]
        while left < right:
            temp = numbers[left] + numbers[right]
            if temp == target:
                return [left+1, right+1]
            if temp < target:
                left += 1
            elif temp > target:
                right -= 1
        return answer