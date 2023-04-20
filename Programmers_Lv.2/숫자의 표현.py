def solution(n):
    answer = 0
    for i in range(1,(n//2)+1):
        c = i
        a = i
        while  c < n:
            a += 1
            c += a
            if c == n:
                answer += 1
    return answer+1