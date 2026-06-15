class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            rock1 = heapq.heappop(stones)
            rock2 = heapq.heappop(stones)

            if rock1 != rock2:
                heapq.heappush(stones, -abs(rock1 - rock2))
            
            print(stones)

        if len(stones) == 1:
            return -stones[0]
        else:
            return 0