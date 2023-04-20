def solution(board, moves):
    answer = 0
    lst = []
    moves = list(map(lambda x: x-1, moves))
    for m in moves:
        for b in board:
            if b[m] == 0:
                continue
            else:
                lst.append(b[m])
                if len(lst) >= 2 and lst[-1] == lst[-2]:
                    lst = lst[:-2]
                    answer += 2
                b[m] = 0
                break
    return answer