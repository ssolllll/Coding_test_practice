def solution(citations):
    answer = []
    for i in range(0,max(citations)+1):
        print(i)
        if len(list(filter(lambda x: x>=i,citations))) >= i and len(list(filter(lambda x: x<=i,citations))) <=i:
            answer.append(i)
        elif max(citations) == 0:
            return 0
    return max(answer)