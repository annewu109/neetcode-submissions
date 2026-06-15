class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            rock1 = heapq.heappop(stones)
            rock2 = heapq.heappop(stones)

            if rock1 != rock2:
                heapq.heappush(stones, rock1 - rock2)

        stones.append(0)
        return -stones[0]