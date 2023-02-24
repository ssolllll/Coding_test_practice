def solution(cipher, code):
    answer = ''
    for v in range(code-1,len(cipher),code):
        answer += cipher[v]
    return answer