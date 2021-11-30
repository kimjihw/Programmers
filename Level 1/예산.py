def solution(d, budget):
    answer = 0
    cnt = 0
    d.sort()
    for i in d:
        if answer <= budget:
            answer += i
            cnt += 1
        else:
            break
    if answer > budget:
        cnt -= 1
    answer = cnt
    print(answer)
    return answer

d = [1,3,2,5,4]
budget = 9
solution(d, budget)