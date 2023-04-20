def solution(a, b, n):
    answer = 0
    if n == a:
        return b
    while n >= a:
        minus = (n//a)*a
        answer += (n//a)*b
        n = n - minus + (n//a)*b
    return answer