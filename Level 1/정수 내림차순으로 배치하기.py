def solution(n):
    answer = 0
    n = list(str(n))
    n.sort()
    n.reverse()
    answer = int("".join(n))

    return answer