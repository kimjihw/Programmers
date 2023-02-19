def solution(my_string):
    answer = ''
    remove = ["a", "e", "i", "o", "u"]
    for i in my_string:
        if i in remove:
           my_string = my_string.replace(i, "")
    answer = my_string
    return answer

my_string = "nice to meet you"
solution(my_string)