def solution(num_list):
    w = 0
    g = 0
    for v in num_list:
        if v%2 == 0:
            g += 1
        else:
            w += 1
    return [g,w]