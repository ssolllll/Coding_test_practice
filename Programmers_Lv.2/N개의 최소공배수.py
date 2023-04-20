def solution(arr):
    a = arr[0]
    for b in range(1,len(arr)):
        e = 1
        b = arr[b]
        c = [a,b]
        if a < b:
            (a,b) = (b,a)
        while b != 0:
            (a,b) = (b,a%b)
        for i in c:
            e *= i//a
        a = e*a
    return a