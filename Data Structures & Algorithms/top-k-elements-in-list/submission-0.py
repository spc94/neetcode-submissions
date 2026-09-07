class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}
        for i in nums:
            if i not in frequent:
                frequent[i] = 1
            else:
                frequent[i] += 1
        sort_kyes_by_their_values = sorted(frequent, key=frequent.get)
        return sort_kyes_by_their_values[-k:]
            



        