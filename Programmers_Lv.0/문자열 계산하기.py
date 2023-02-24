def solution(my_string):
    my_string = my_string.split(' ')
    answer = int(my_string[0])
    my_string = my_string[1:]
    while len(my_string) != 0:
        if my_string[0] == '+':
            answer += int(my_string[1])
            my_string = my_string[2:]
        elif my_string[0] == '-':
            answer -= int(my_string[1])
            my_string = my_string[2:]
    return answer