class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for point in points:
            distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(pq, (distance, point))

        res = []
        for _ in range(k):
            priority, point = heapq.heappop(pq)
            res.append(point)
        return res