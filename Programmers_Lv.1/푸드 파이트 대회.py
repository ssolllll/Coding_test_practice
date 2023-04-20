def solution(food):
    answer = ''
    answer_2 = ''
    for ind in range(1,len(food)):
        answer += f'{ind}'*(food[ind]//2)
        answer_2 = f'{ind}'*(food[ind]//2)+answer_2
    return answer+'0'+answer_2