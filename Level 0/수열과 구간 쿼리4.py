def solution(arr, queries):
    answer = []
    for i in queries:
        for j in range(i[0], i[1] + 1):
            if j % i[2] == 0:
                arr[j] += 1
    return answer


solution([0, 1, 2, 4, 3], [[0, 4, 1], [0, 3, 2], [0, 3, 3]])
