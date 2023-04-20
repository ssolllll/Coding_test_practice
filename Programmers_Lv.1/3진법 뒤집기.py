def solution(n):
    conv = ''
    while n >0:
        n, mod = divmod(n, 3)
        conv += str(mod)
    return int(conv,3)