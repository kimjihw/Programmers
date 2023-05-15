def solution(q, r, code):
    answer = ''

    for i in range(len(code)):
        if i % q == r:
            answer += code[i]
    return answer


solution(3, 1, "qjnwezgrpirldywt")
