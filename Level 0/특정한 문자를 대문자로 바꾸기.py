def solution(my_string, alp):
    answer = ''
    for i in my_string:
        if i == alp.upper() or i == alp.lower():
            answer += i.upper()
        else:
            answer += i.lower()

    return answer

solution("programmers", "p")