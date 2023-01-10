import math

def solution(balls, share):
    answer = 0

    fac1 = math.factorial(balls)
    fac2 = math.factorial(balls - share) * math.factorial(share)

    answer = int(fac1 / fac2)

    return answer

balls = 3
share = 2
solution(balls, share)