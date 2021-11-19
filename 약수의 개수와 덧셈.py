def solution(left, right):
    answer = 0
    div = []
    odd = []
    even = []
    for i in range(left, right + 1):
        num = []
        for j in range(1, i + 1):
            if i % j == 0:
                num.append(j)
        div.append(num)

    for i in range(len(div)):
        if len(div[i]) % 2 == 0:
            even.append(max(div[i]))
        else:
            odd.append(max(div[i]))

    answer += sum(even) - sum(odd)
    return answer