def solution(x):
    answer = True
    original = x
    result = 0
    x = list(str(x))
    for i in x:
        result += int(i)

    if original % result == 0:
        answer = True
    else:
        answer = False
    return answer