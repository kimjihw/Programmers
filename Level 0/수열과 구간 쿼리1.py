def solution(arr, queries):
    answer = []
    for s, e in queries:
        for i in range(s, e+1):
            arr[i] += 1

    answer = arr

    return answer


solution([0, 1, 2, 3, 4], [[0, 1], [1, 2], [2, 3]])
