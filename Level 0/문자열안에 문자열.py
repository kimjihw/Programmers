def solution(str1, str2):
    answer = 0
    if str2 in str1:
        answer = 1
    else:
        answer = 2
    return answer

str1 = "ab6CDE443fgh22iJKlmn1o"
str2 = "6CD"
solution(str1, str2)