def solution(a, b):
    answer = 0
    plus = int(str(a)+str(b))
    multi = 2 * a * b

    if plus > multi:
        answer = plus
    else:
        answer = multi

    return answer

solution(2, 91)