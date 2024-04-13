class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        res = 0
        set_nums = set(nums)
        for num in nums:
            if (num - 1) not in set_nums: # start of sequence
                current = 1
                while (current+num) in set_nums: # find range
                    current += 1
                res = max(res, current)
        
        return res
