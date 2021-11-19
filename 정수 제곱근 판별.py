def solution(n):
    answer = 0

    k = int(n ** 0.5)

    if n == k * k:
        n += 1
        answer = (k + 1) * (k + 1)
    else:
        answer += -1
    return answer