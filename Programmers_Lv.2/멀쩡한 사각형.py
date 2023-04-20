import math
def solution(w,h):
    if w == h:
        return w*h -w
    elif w ==1 or h ==1:
        return 0
    else:
        a = 0
        for x,y in zip(range(w),range(1,w+1)):
            a += math.ceil(h-(h*x/w))- math.floor(h-(h*y/w))
        return h*w-a