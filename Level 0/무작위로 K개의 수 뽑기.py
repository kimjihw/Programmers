def solution(arr, k):
    answer = []
    for i in range(len(arr)):
        if arr[i] not in answer:
            answer.append(arr[i])
    if len(answer) >= k:
        answer = answer[:k + 1]
    else:
        answer.extend([-1] * (k - len(answer)))

    return answer


solution([0, 1, 1, 1, 1], 4)
