def solution(my_string):
    answer = ''
    for i in list(dict.fromkeys(my_string)):
        answer += i
    return answer

my_string = "people"
solution(my_string)