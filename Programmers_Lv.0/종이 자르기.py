def solution(M, N):
    answer = 0
    if M == 1 and N == 1:
        return 1
    if M > N:
        M,N = N,M
    answer += M-1
    answer += (N-1)*M
    return answer