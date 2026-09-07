class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        nums_sorted = sorted(self.nums, reverse = True)
        return nums_sorted[self.k-1]
        
