def solution(order):
    answer = 0
    for i in order:
        if "cafelatte" in i:
            answer += 5000
        else:
            answer += 4500
    print(answer)
    return answer

solution(["cafelatte", "americanoice", "hotcafelatte", "anything"])