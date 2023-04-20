def solution(number):
    n = 0
    a = 1
    while True:
        if number > n and number <=n+(3**a):
            break
        else:
            n += 3**a
            a += 1
    answer = ""
    number = number-n-1
    if number >= 3:
        while number // 3 >= 1:
            remain = number % 3
            number = number // 3
            answer = str(remain) + answer
            if number < 3 :
                answer = str(number) + answer
    else:
        answer += str(number)
    answer = '0'*(a-len(answer)) + answer
    answer = answer.replace("2", "4")
    answer = answer.replace("1", "2")
    answer = answer.replace("0", "1")
    return answer