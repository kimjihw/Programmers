from collections import Counter


def solution(array):
    answer = 0
    lst = Counter(array)
    order = lst.most_common()
    maximum = order[0][1]

    modes = []
    if len(array) == 1:
        answer = array[0]
    else:
        for i in lst.most_common():
            if i[1] == maximum:
                modes.append(i[0])
        if len(modes) == 1:
            answer = modes[0]
        else:
            answer = -1
    return answer


solution([12, 44, 3, -1, 1, 0, 0])
