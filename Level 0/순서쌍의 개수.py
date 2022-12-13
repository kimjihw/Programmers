def solution(n):
    answer = 0
    cnt = []
    for i in range(1, n + 1):
        if n % i == 0:
            cnt.append(i)
            cnt.append(n / i)
    answer = len(cnt) / 2
    return answer

n = 20

solution(n)