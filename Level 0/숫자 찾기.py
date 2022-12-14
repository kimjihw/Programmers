def solution(num, k):
    answer = 0
    num_str = str(num)
    if str(k) in num_str:
        answer = num_str.index(str(k)) + 1
    else:
        answer = -1
    return answer

num = 232443
k = 4
solution(num, k)