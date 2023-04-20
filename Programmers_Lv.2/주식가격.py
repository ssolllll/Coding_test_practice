def solution(prices):
    answer = []
    for x,y in zip(range(len(prices)),range(1,len(prices))):
        if prices[x] > prices[y]:
            answer.append(1)
            pass
        else:
            a  = 0
            while y <= len(prices)-1:
                if prices[x] <= prices[y]:
                    a += 1
                    y += 1
                elif prices[x] > prices[y]:
                    a += 1
                    break
            answer.append(a)
    answer.append(0)
    return answer