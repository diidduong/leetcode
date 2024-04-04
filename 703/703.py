import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        if nums:
            nums.sort()
            nums = nums[-k:]
            heapq.heapify(nums)
        self.nums = nums

    def add(self, val: int) -> int:
        if len(self.nums) < self.k or val > self.nums[0]:
            heapq.heappush(self.nums, val)
            if len(self.nums) > self.k:
                heapq.heappop(self.nums)
        return self.nums[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
