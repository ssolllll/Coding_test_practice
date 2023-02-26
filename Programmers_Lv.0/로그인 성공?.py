def solution(id_pw, db):
    answer = 'fail'
    for x,y in db:
        if id_pw[0]== x and id_pw[1] == y:
            return "login"
        elif id_pw[0] == x and id_pw[1] != y:
            answer = 'wrong pw'
    return answer