def solution(cipher, code):
    answer = ''
    answer += cipher[code-1:len(cipher):code]
    return answer

cipher = "dfjardstddetckdaccccdegk"
code = 4
solution(cipher, code)