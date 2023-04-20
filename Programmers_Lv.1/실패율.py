def solution(N,stages):
    failure = {}
    l = len(stages)
    for stage in range(1,N+1):
        if l != 0:
            failure[stage] = stages.count(stage)/l
            l -= stages.count(stage)
        else:
            failure[stage] = 0
    return sorted(failure, key = lambda x: failure[x],reverse=True)