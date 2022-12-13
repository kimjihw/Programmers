def solution(money):
    answer = []
    cnt = int(money/ 5500)
    answer.append(cnt)
    answer.append(money - (5500 * cnt))

    return answer

money = 15000
solution(money)