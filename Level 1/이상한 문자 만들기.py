def solution(s):
    answer = ''
    lst = []
    lst.extend(s.split(" "))

    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if j % 2 == 0:
                answer += lst[i][j].upper()
            else:
                answer += lst[i][j].lower()
        answer += ' '
    answer = answer[0:len(answer)-1]
    return answer