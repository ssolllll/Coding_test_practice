def solution(answers):
    ret = []
    math_1 = [1,2,3,4,5]
    math_2 = [2,1,2,3,2,4,2,5]
    math_3 = [3,3,1,1,2,2,4,4,5,5]
    math = [math_1, math_2, math_3]
    lst = []
    for i in math:
        score = 0
        if len(answers) > len(i):
            for x,y in zip(answers,(i*(len(answers)//len(i)+1))):
                if x == y:
                    score += 1
                else:
                    pass
            lst.append(score)
        elif len(answers) <= len(i):
            for x,y in zip(answers,i):
                if x == y:
                    score += 1
                else:
                    pass
            lst.append(score)
        print(score)
    for i,k  in zip(lst, range(1,len(lst)+1)):
        if max(lst) == i:
            ret.append(k)
        else:
            pass
    return ret