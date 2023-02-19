def solution(rsp):
    answer = ''
    slst = list(rsp)
    dic = {"2": "0", "0": "5", "5": "2"}
    for i in slst:
        answer += dic.get(i)

    return str(answer)


rsp = "205"
solution(rsp)
