def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        answer += my_string[i]
    return answer

solution("zpiaz", [1, 2, 0, 0, 3])