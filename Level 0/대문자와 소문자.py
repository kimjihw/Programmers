def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            i = i.lower()
            answer += i
        else:
            i = i.upper()
            answer += i

    return answer

my_string = "CCuu"
solution(my_string)