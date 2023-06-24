def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        lst = []
        for i in range(s, e + 1):
            if arr[i] > k:
                lst.append(arr[i])
        if len(lst) == 0:
            answer.append(-1)
        else:
            answer.append(min(lst))

    return answer


solution([0, 1, 2, 4, 3], [[0, 4, 2], [0, 3, 2], [0, 2, 2]])
