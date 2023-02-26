def solution(numbers, k):
    answer = 0
    c = 0
    for _ in range(k):
        try:
            numbers[c]
            answer = c
        except:
            c -= len(numbers)
            answer = c
        c += 2
    return answer+1