def s(num):
    return (num*(num+1))//2

def solution(num, total):
    answer = []
    total -= s(num-1)
    x = total//num
    return [x +i for i in range(num)]