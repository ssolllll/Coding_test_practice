def solution(n, arr1, arr2):
    answer = []
    for x,y in zip(arr1, arr2):
        string = ""
        for i,k in zip((bin(x)[2:].zfill(n)),(bin(y)[2:].zfill(n))):
            if int(i)+int(k) != 0:
                string += ("#")
            else:
                string += (" ")
        answer.append(string)
    return answer