def solution(quiz):
    answer = []

    for i in quiz:
        if int(eval(i.split("=")[0])) == int(i.split("=")[-1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer

quiz = ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]
solution(quiz)