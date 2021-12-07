def solution(s):
    answer = ''
    s = s.split(" ")
    lst = []
    for i in s:
        lst.append(int(i))
    answer += str(min(lst)) + " " + str(max(lst))
    print(answer)
    return answer

s = "-1 -2 -3 -4"
solution(s)