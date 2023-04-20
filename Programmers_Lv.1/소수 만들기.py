from itertools import combinations
def solution(nums):
    c = 0
    a = list(combinations(nums, 3))
    for i in a:
        if sum(i) % 2 == 0:
            pass
        else:
            for k in range(2,sum(i)):
                if sum(i) % k != 0:
                    b = 1
                elif sum(i) % k == 0:
                    b = 0
                    break
            if b == 1:
                c += 1
    return c