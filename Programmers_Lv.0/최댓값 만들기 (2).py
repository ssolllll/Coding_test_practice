def solution(numbers):
    answer = 0
    if len(numbers) == 2:
        return numbers[0]*numbers[1]
    for x,k in enumerate(numbers):
        for y,v in enumerate(numbers):
            if x == y:
                continue
            else:
                if answer < k*v:
                    answer = k*v
    return answer