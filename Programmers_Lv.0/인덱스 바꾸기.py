def solution(my_string, num1, num2):
    answer = ''
    answer += my_string[num1]
    answer += my_string[num2]
    if num1 < num2:
        my_string = my_string[:num1]+answer[1]+my_string[num1+1:num2]+answer[0]+my_string[num2+1:]
    else:
        my_string = my_string[:num2]+answer[1]+my_string[num2+1:num1]+answer[0]+my_string[num1+1:]
    return my_string