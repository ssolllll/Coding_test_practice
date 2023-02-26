def solution(n):
    answer = 0
    if 1<= n <=3:
        return 0
    else:
        for v in range(4,n+1):
            c = 0
            for k in range(1,v+1):
                if v%k==0:
                    c += 1
            if c >=3:
                answer += 1
    return answer