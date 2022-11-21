def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdecimal():
            answer.append(int(i))
            answer.sort()
    
    return answer

answer = "hi12392"
solution(answer)