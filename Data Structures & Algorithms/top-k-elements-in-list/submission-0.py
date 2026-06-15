class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        encountered = defaultdict(int)
        for num in nums:
            encountered[num] = encountered[num] + 1
        
        pq = []
        for key, value in encountered.items():
            heapq.heappush(pq, (value * -1, key))
        
        res = []
        for _ in range(k):
            value, key = heapq.heappop(pq)
            res.append(key)

        return res


        