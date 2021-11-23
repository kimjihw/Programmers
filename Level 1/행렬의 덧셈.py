def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        lst = []
        answer.append(lst)
        for j in range(len(arr1[i])):
            lst.append(arr1[i][j] + arr2[i][j])

    return answer