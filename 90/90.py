class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], nums]

        res = [[]]
        sub = []
        nums.sort()
        def dfs(nums, i):
            if i >= len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            dfs(nums, i+1)

            sub.pop()
            ii = i+1
            while ii < len(nums) and nums[ii] == nums[i]:
                ii += 1
            dfs(nums, ii)
        
        dfs(nums, 0)
        res.pop()
        return res
