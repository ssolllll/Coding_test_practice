def solution(numbers):
    answer = ''
    dic = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5'
          ,'six':'6','seven':'7','eight':'8','nine':'9'}
    while len(numbers) != 0:
        for value in range(1,len(numbers)+1):
            try:
                answer += dic[numbers[:value]]
                numbers = numbers[value:]
            except:
                continue
    return int(answer)