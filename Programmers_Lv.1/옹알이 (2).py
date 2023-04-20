def solution(babbling):
    answer = 0
    bab = ['woo','ye','ma','aya']
    for babble in babbling:
        for b in bab:
            if b*2 not in babble:
                babble = babble.replace(b,' ')
        if babble.strip() == '':
            answer += 1
    return answer