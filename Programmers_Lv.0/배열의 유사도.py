def solution(s1, s2):
    answer =0
    for v in s1:
        for k in s2:
            if v == k:
                answer += 1
    return answer