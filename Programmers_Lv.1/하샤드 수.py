def solution(x):
    answer = True
    if x % sum(list(map(lambda x: int(x), list(str(x))))) != 0:
        answer = False
    return answer