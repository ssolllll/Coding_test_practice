def solution(n):
    for v in range(1,n+1):
        if 1<=n<=3:
            return 1
        elif n == 4:
            return 2
        elif n == 5:
            return 5
        elif (n*v)%6 == 0:
            return n*v//6