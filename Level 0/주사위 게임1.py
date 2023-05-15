def solution(a, b):
    answer = 0
    one, two, three = (a ** 2 + b ** 2), 2 * (a + b), abs(a - b)

    if a % 2 != 0 and b % 2 != 0:
        answer = one
    elif a % 2 != 0 or b % 2 != 0:
        answer = two
    else:
        answer = three
    return answer


solution(3, 5)
