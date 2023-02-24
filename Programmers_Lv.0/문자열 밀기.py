def solution(A, B):
    answer = -1
    a = len(A)
    c = 0
    for _ in range(len(B)):
        if A == B:
            return c
        else:
            A = A[a-1]+A[0:a-1]
            c += 1
    if A == B:
        return c
    return answer