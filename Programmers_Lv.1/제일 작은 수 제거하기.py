def solution(arr):
    if len(arr) == 1:
        answer = [-1]
        return answer
    else:
        del arr[arr.index(min(arr))]
    return arr