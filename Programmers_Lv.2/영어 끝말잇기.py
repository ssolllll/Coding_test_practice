def solution(n,words):
    c = 0
    answer = []
    for x, value in enumerate(words):
        if x == 0:
            answer.append(value)
            c += 1
            continue
        elif (value not in answer) and answer[-1][-1] == value[0]:
            answer.append(value)
            c += 1
        else:
            return[(c%n)+1,c//n+1]
    if c == len(words):
        return [0,0]