def solution(order):
    answer = 0
    lst = [3, 6, 9]
    slst = list(str(order))
    for i in slst:
        if int(i) in lst:
            answer += 1
    print(answer)
    return answer


order = 3333
solution(order)
