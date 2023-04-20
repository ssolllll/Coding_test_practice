import heapq
def solution(s, K):
    answer = 0
    s.sort()
    while s[0] < K:
        if len(s) <= 1:
            return -1
        else:
            a = heapq.heappop(s)
            heapq.heappush(s, a+(heapq.heappop(s))*2)
            answer += 1
    return answer