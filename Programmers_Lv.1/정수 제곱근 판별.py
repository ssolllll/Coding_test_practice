import numpy as np
def solution(n):
    if int(np.sqrt(n))**2 == n:
        answer = int((np.sqrt(n)+1)**2)
    else:
        answer = -1
    return answer