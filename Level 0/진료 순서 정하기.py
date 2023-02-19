def solution(emergency):
    answer = []
    rst = sorted(emergency, reverse=True)

    for i in emergency:
        answer.append(rst.index(i) + 1)

    return answer


emergency = [3, 76, 24]
solution(emergency)
