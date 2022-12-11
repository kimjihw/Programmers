def solution(my_string, num1, num2):
    answer = ''
    listString = list(my_string)
    listString[num1], listString[num2] = listString[num2], listString[num1]
    answer = "".join(listString)
    return answer

my_string = "hello"
num1 = 1
num2 = 2
solution(my_string, num1, num2)