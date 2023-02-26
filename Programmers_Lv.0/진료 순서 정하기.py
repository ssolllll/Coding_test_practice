def solution(emergency):
    answer = [0 for v in range(len(emergency))]
    c = 1
    for _ in range(len(emergency)):
        print(max(emergency))
        for x,k in enumerate(emergency):
            if max(emergency) == k:
                emergency[x] = 0
                answer[x] = c
                c += 1
                break
    return answer