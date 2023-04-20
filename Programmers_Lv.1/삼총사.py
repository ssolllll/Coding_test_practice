def solution(number):
    answer = 0
    for m,x in enumerate(number):
        for n,y in enumerate(number[m+1:],start=m+1):
            for k,z in enumerate(number[n+1:],start=n+1):
                if m==n or n==k or k==m:
                    continue
                elif x+y+z == 0:
                    answer += 1
    return answer