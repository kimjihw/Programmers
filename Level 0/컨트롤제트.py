def solution(s):
    answer = 0
    lst = []
    lst.extend(s.split(" "))
    rst = []
    for i in lst:
        if i == "Z":
           rst.pop()
        else:
            rst.append(int(i))
    answer = sum(rst)
    return answer

solution("1 2 Z 3")