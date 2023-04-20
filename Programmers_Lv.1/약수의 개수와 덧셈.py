def fnd(n):
    cnt = 0
    for i in range(1,n+1):
        if n%i == 0:
            cnt += 1
    return cnt

def solution(left, right):
    answer = 0
    for value in range(left,right+1):
        if fnd(value) % 2 == 0:
            answer += value
        elif fnd(value) % 2 == 1:
            answer -= value
    return answer