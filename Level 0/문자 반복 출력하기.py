def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i*3

    return answer

my_string = "hello"
n = 3
solution(my_string, n)