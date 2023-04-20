def solution(brown,yellow):
    answer = []
    for w in range(1,yellow+1):
        if (yellow/w) != (yellow//w):
            pass
        elif w < int(yellow/w):
            pass
        else:
            if brown == 2*(yellow//w)+2*w+4:
                answer.append(w+2)
                answer.append((yellow//w)+2)
    return answer