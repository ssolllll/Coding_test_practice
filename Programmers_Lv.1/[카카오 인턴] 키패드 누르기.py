def solution(numbers, hand):
    answer = ''
    L = "*"
    R = "#"
    lst = []
    for i in range(1,4):
        for k in range(1,4):
            lst.append((i,k))
    int_list = [1,2,3,4,5,6,7,8,9]
    dic = dict(zip(int_list,lst))
    dic['*'] = (4,1)
    dic['#'] = (4,3)
    dic[0] = (4,2)
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            L = num
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            R = num
        elif num == 2 or num == 5 or num == 8 or num == 0:
            if abs(dic[L][0] - dic[num][0]) + abs(dic[L][1] - dic[num][1]) < abs(dic[R][0] - dic[num][0]) + abs(dic[R][1] - dic[num][1]):
                answer += 'L'
                L = num
            elif abs(dic[L][0] - dic[num][0]) + abs(dic[L][1] - dic[num][1]) > abs(dic[R][0] - dic[num][0]) + abs(dic[R][1] - dic[num][1]):
                answer += 'R'
                R = num
            elif abs(dic[L][0] - dic[num][0]) + abs(dic[L][1] - dic[num][1]) == abs(dic[R][0] - dic[num][0]) + abs(dic[R][1] - dic[num][1]):
                if hand == "right":
                    answer += 'R'
                    R = num
                else:
                    answer += 'L'
                    L = num
    return answer