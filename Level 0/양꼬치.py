def solution(n, k):
    answer = 0
    k -= int(n / 10)
    answer = (n * 12000) + (k * 2000)

    return answer

n = 64
k = 6
solution(n, k)