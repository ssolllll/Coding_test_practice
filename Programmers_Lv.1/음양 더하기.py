def solution(absolutes, signs):
    for x in range(len(absolutes)):
        if signs[x] == False:
            absolutes[x] = -absolutes[x]
        elif signs[x] == True:
            continue
    return sum(absolutes)