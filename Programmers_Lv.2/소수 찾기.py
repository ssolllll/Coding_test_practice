from itertools import permutations
def solution(numbers):
    answer = []
    ant = 0
    for k in range(1,len(numbers)+1):
        for i in list(map(lambda x: list(x), (permutations(numbers, k)))):
            a = ''
            for x in i:
                a += x
            answer.append(int(a))
    for j in list(set(answer)):
        cnt = 0
        if j == 2 or j == 3:
            ant += 1
        elif j % 2 == 0:
            pass
        else:
            for y in range(3,j,2):
                if j % y == 0:
                    cnt = 0
                    break
                else:
                    cnt = 1
                    pass
        if cnt == 1:
            ant += 1
    return ant