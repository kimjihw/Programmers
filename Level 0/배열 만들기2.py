from itertools import product

def solution(l, r):
    answer = []
    for i in product([0, 5], repeat=len(str(r))):
        lst = list(i)
        s = ""
        for j in lst:
            s += str(j)
        if l <= int(s) <= r:
            answer.append(int(s))
    if len(answer) == 0:
        return [-1]

    return answer


solution(5, 555)
