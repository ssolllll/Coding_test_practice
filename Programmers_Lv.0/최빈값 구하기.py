def solution(array):
    answer = 0
    m = 0
    for value in set(array):
        if array.count(value) > answer:
            answer = array.count(value)
            m = value
        elif array.count(value) == answer:
            m = -1
    return m