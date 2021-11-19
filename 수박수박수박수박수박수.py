def solution(n):
    answer = ''
    lst = '수박'*n
    lst = list(lst)

    for i in range(n):
        answer += lst[i]
    return answer