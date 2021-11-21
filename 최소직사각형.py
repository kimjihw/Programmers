def solution(sizes):
    answer = 0

    x = []
    y = []
    for i in sizes:
        if i[0] < i[1]:
            i[0], i[1] = i[1], i[0]
        x.append(i[1])
        y.append(i[0])
    answer = max(x) * max(y)
    return answer

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
solution(sizes)