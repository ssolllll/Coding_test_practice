def solution(s):
    return f'{min(list(map(lambda x: int(x), s.split())))} {max(list(map(lambda x: int(x), s.split())))}'