class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        # index 를 담아서 리턴한다
        N = len(nums)
        for i in range(N-1):
            for j in range(i+1, N):
                if nums[i] + nums[j] == target:
                    answer.append(i)
                    answer.append(j)
        return answer