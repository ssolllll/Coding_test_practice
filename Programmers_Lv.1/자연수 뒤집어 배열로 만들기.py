def solution(n):
    lst = []
    answer = []
    lst.extend(str(n))
    for i in lst:
        answer.append(int(i))
    print(answer)
    answer.reverse()
    return answer