def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer

array = [149, 180, 192, 170]
height = 167
solution(array, height)