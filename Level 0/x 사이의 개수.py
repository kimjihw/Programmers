def solution(myString):
    answer = []
    lst = []
    lst.extend(myString.split("x"))

    for i in lst:
        answer.append(len(i))
    print(answer)
    return answer

solution("oxooxoxxox")