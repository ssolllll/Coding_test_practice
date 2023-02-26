def solution(dots):
    answer = 0
    lst = [[[0,1],[2,3]],[[0,2],[1,3]],[[0,3],[1,2]]]
    for x,y in lst:
        if (dots[x[0]][0]-dots[x[1]][0])/(dots[x[0]][1]-dots[x[1]][1]) == (dots[y[0]][0]-dots[y[1]][0])/(dots[y[0]][1]-dots[y[1]][1]):
            return 1
    return answer