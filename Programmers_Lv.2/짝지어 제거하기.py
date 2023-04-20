from collections import deque

def solution(s):
    queue = deque()
    for value in range(len(s)):
        if value == 0:
            queue.append(s[value])
        elif len(queue) == 0:
            queue.append(s[value])
        else:
            if s[value] == queue[-1]:
                queue.pop()
            else:
                queue.append(s[value])
    if len(queue) == 0:
        return 1
    else:
        return 0