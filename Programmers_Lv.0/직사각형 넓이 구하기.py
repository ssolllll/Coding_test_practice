def solution(dots):
    answer = 0
    for x in dots:
        for y in dots:
            if (x[0]-y[0])*(x[1]-y[1]) >= answer:
                answer = (x[0]-y[0])*(x[1]-y[1])
    return answer