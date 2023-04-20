def solution(tri):
    for ind in range(1,len(tri)):
        for i in range(0,len(tri[ind])):
            if i == 0:
                tri[ind][0] += tri[ind-1][0]
            elif i == ind:
                tri[ind][i] += tri[ind-1][i-1]
            else:
                tri[ind][i] += max(tri[ind-1][i],tri[ind-1][i-1])
    return max(tri[-1])