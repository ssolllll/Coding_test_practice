def solution(num_list, n):
    answer = []
    for v in range(0,len(num_list)//n):
        answer.append(num_list[0+(n*v):n+(n)*v])
    return answer