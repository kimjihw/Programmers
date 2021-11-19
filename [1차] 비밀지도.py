def solution(n, arr1, arr2):
    answer = []
    lst = []
    for i in range(n):
        lst.append(str(int(format(arr1[i], 'b')) + int(format(arr2[i], 'b'))))

    for i in lst:
        if len(i) < n:
            i = (n - len(i)) * '0' + i
        i = i.replace("2", "1")
        i = i.replace("1", "#")
        i = i.replace("0", " ")
        answer.append(i)
    return answer