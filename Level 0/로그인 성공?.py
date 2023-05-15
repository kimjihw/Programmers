def solution(id_pw, db):
    answer = ''
    idx = 0
    for i in db:
        if id_pw[0] in i:
            idx = db.index(i)
    if id_pw in db:
        answer = 'login'
    elif id_pw[0] == db[idx][0] and id_pw[1] != db[idx][1]:
        answer = "wrong pw"
    else:
    
        answer = "fail"
    return answer

id_pw = ["rabbit04", "98761"]
db = [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]
solution(id_pw, db)