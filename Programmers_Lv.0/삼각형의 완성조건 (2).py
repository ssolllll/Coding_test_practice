def solution(sides):
    answer = 0
    a = sides[0]
    b = sides[1]
    if a > b:
        a,b = b,a
    return a*2-1