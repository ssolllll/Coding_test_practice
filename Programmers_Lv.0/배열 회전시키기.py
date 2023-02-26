def solution(numbers, d):
    if d == 'right':
        answer = [numbers[-1]]
        for v in numbers[:len(numbers)-1]:
            answer.append(v)
        return answer
    else:
        answer = numbers[1:]
        answer.append(numbers[0])
        return answer