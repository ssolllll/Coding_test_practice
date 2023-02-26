def solution(boards):
    n = len(boards)
    answer = [[0 for _ in range(n)] for _ in range(n)]
    xy = [[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1]]
    bomb_lst = []
    for board_idx in range(len(boards)):
        for b_idx in range(len(boards[board_idx])):
            if boards[board_idx][b_idx] == 1:
                bomb_lst.append([board_idx,b_idx])
    for boom in bomb_lst:
        answer[boom[0]][boom[1]] = 1
        for x,y in xy:
            a,b = boom[0]+x, boom[1]+y
            if a <0 or b < 0 or a > len(answer)-1 or b > len(answer)-1:
                continue
            else:
                answer[a][b] = 1
    answer = [sum(ans) for ans in answer]
    return len(boards)**2-sum(answer)