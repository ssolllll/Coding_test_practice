def solution(denum1, num1, denum2, num2):
    answer = []
    denum1, num1, denum2, num2 = denum1*num2, num1*num2, denum2*num1, num2*num1
    answer = [denum1+denum2,num1]
    while True:
        a = answer[0]
        for value in range(2,answer[0]+1):
            if answer[0] % value == 0 and answer[1] % value == 0:
                answer[0] //= value
                answer[1] //= value
                break
        if answer[0] == a:
            break
    return answer