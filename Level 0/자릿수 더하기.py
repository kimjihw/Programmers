def solution(n):
    answer = 0
    stringN = str(n)
    for i in stringN:
        answer += int(i)
    print(answer)
    return answer

n = 1234