def solution(arr, delete_list):
    answer = []

    for i in delete_list:
        if i in arr:
            arr.remove(i)

    answer = arr
    return answer

solution([293, 1000, 395, 678, 94], [94, 777, 104, 1000, 1, 12])