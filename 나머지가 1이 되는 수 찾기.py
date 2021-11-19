def solution(n):
    answer = 0
    lst = []
    for i in range(2, n + 1):
        if n % i == 1:
            lst.append(i)
    answer = min(lst)
    return answer