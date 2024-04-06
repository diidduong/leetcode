class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        current = []
        candidates.sort()

        def pickornot(candidates, i, csum, target):
            if csum == target:
                res.append(current.copy())
                return
            
            if csum > target or i >= len(candidates):
                return
            
            current.append(candidates[i])
            pickornot(candidates, i+1, csum + candidates[i], target)

            current.pop()
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            
            pickornot(candidates, j, csum, target)

        pickornot(candidates, 0, 0, target)
        return res
