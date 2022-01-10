def solution(n):
    answer = 0
    lst = [0] * (n + 1)
    lst[1] = 1
    lst[2] = 2
    for i in range(2, n + 1):
        lst[i] = lst[i - 1] + lst[i - 2]
    answer = lst[n] % 1234567
    return answer

n = int(input())
solution(n)