def solution(n,left,right):
    answer =[]
    for num in range(left,right+1):
        if (num//n)+1 > (num%n):
            answer.append((num//n)+1)
        elif num% n==0:
            answer.append(n)
        else:
            answer.append((num%n)+1)
    return answer