def solution(i, j, k):
    answer = 0
    string = ""
    for r in range(i, j + 1):
        string += str(r)
    answer = string.count(str(k))
    return answer

i = 1
j = 13
k = 1
solution(i, j, k)