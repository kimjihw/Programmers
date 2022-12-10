import math


def solution(n):
    answer = 0
    math.sqrt(n)
    if math.sqrt(n) != int(math.sqrt(n)):
        answer = 2
    else: answer = 1
    return answer

n = 144
solution(n)