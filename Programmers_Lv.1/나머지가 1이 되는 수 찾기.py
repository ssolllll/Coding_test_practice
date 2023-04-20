def solution(n):
    for value in range(2,n):
        if (n-1)%value == 0:
            return value