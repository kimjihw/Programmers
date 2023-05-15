def solution(str_list):
    answer = []
    l = str_list.index("l")
    r = str_list.index("r")
    if l < r:
        answer = str_list[0 : l]
    else:
        answer = str_list[r : :]
    print(answer)
    return answer

str_list = ["u", "u", "l", "r"]
solution(str_list)