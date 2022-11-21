def solution(array):
    answer = 0
    array = sorted(array)
    answer = array[int(len(array)/ 2)]

    return answer

array = [9, -1, 0]
solution(array)