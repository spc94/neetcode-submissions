class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums_minHeap = nums
        heapq.heapify(self.nums_minHeap)
        while len(self.nums_minHeap) > k:
            heapq.heappop(self.nums_minHeap)

    def add(self, val: int) -> int:
        #self.nums.append(val)
        #nums_sorted = sorted(self.nums, reverse = True)
        #return nums_sorted[self.k-1]
        heapq.heappush(self.nums_minHeap, val)
        if len(self.nums_minHeap) > self.k:
            heapq.heappop(self.nums_minHeap)
        return self.nums_minHeap[0] #smallest value
        
