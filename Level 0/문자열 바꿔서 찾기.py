def solution(myString, pat):
    answer = 0
    change = ""
    for i in myString:
        if i == "A":
            change += "B"
        else:
            change += "A"
    if pat in change:
        answer = 1
    else:
        answer = 0
    return answer

solution("ABAB", "ABAB")