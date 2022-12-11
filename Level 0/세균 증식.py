def solution(n, t):
    answer = 0
    for i in range(t):
        n *= 2
    answer = n
    return answer

n = 7
t = 15
solution(n, t)