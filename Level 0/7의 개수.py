def solution(array):
    answer = 0
    string = ""
    for i in array:
        string += str(i)

    answer = string.count("7")

    return answer

array = [7, 77, 17]
solution(array)