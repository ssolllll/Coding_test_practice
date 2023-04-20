def solution(d, budget):
    while budget < sum(d):
        del d[d.index(max(d))]
    return len(d)