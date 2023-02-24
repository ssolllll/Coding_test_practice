def solution(num, k):
    if int(str(num).find(str(k)))+1 != 0:
        return int(str(num).find(str(k)))+1
    else:
        return -1