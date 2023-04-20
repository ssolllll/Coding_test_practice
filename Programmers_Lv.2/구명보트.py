from collections import deque

def solution(p, limit):
    answer = 0
    dq = deque(sorted(p,reverse = True))
    while len(dq) != 0:
        if len(dq) == 1:
            dq.pop()
            answer += 1
        elif dq[0]+dq[-1] <= limit:
            dq.pop()
            dq.popleft()
            answer += 1
        else:
            dq.popleft()
            answer += 1
    return answer