import heapq
def solution(n, works):
    if sum(works) < n:
        return 0
    max_heap = []
    for item in works:
        heapq.heappush(max_heap, -item)
    for _ in range(n):
        heapq.heappush(max_heap,(heapq.heappop(max_heap)+1))
    answer = [ind**2 for ind in max_heap]
    return sum(answer)