def solution(keyinput, board):
    answer = [0,0]
    limit_1 = board[0]//2
    limit_2 = board[1]//2
    for value in keyinput:
        if value == 'left':
            if abs(answer[0]) == limit_1:
                if answer[0] == limit_1:
                    answer[0] -= 1
                else:
                    pass
            else:
                answer[0] -= 1
        elif value == 'right':
            if abs(answer[0]) == limit_1:
                if answer[0] != limit_1:
                    answer[0] += 1
                else:
                    pass
            else:
                answer[0] += 1
        elif value == 'up':
            if abs(answer[1]) == limit_2:
                if answer[1] != limit_2:
                    answer[1] += 1
                else:
                    pass
            else:
                answer[1] += 1
        elif value == 'down':
            if abs(answer[1]) == limit_2:
                if answer[1] == limit_2:
                    answer[1] -= 1
                else:
                    pass
            else:
                answer[1] -= 1
    return answer