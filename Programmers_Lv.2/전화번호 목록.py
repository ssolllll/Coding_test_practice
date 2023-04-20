def solution(phone_book):
    answer = True
    dic = {}
    phone_book = sorted(phone_book)
    for x,y in enumerate(phone_book):
        dic[x] = y
    for x in range(0,len(dic.keys())):
        try:
            if dic[x+1].startswith(dic[x]):
                return False
                break
        except:
            pass
    return answer