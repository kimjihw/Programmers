def solution(n):
    answer = []
    n = str(n)
    n = n[::-1]
    n = list(n)
    for i in n:
        i = int(i)
        answer.append(i)
    return answer