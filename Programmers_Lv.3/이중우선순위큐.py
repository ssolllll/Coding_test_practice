import heapq
def solution(operations):
    max_heap = []
    min_heap = []
    heapq.heapify(max_heap)
    heapq.heapify(min_heap)
    for ind in operations:
        i = ind.split()
        if i[0] == 'I':
            heapq.heappush(min_heap, int(i[1]))
            heapq.heappush(max_heap, -int(i[1]))
        elif len(max_heap) == 0:
            continue
        elif i[1] == '1': # 1인 경우
            ma = heapq.heappop(max_heap)
            a = min_heap.index(-ma)
            min_heap.pop(a)
        else: # -1인 경우
            mi = heapq.heappop(min_heap)
            a = max_heap.index(-mi)
            max_heap.pop(a)
    if len(min_heap) == 0:
        return [0,0]
    else:
        return [-max_heap[0], min_heap[0]]