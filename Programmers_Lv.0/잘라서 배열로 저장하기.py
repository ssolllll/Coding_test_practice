def solution(my_str, n):
    answer = []
    if len(my_str)%n == 0:
        for value in range(len(my_str)//n):
            answer.append(my_str[value*n:(value+1)*n])
    else:
        for value in range(len(my_str)//n+1):
            answer.append(my_str[value*n:(value+1)*n])
    return answer