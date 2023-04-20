def solution(a,b):
    c = [a,b]
    d = []
    e = 1
    if a<b:
        (a,b) = (b,a)
    while b !=0:
        (a,b) = (b,a%b)
    d.append(a)
    for i in c:
        e *= i//a
    d.append(e*a)
    return d