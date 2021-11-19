def solution(n, m):
    answer = []
    div1 = []
    div2 = []
    mul1 = []
    mul2 = []

    for i in range(1, n + 1):
        if n % i == 0:
            div1.append(i)
    for i in range(1, m + 1):
        if m % i == 0:
            div2.append(i)
    for i in range(1, m + 1):
        mul1.append(n*i)
        mul2.append(m*i)
    div1 = set(div1)
    div2 = set(div2)
    mul1 = set(mul1)
    mul2 = set(mul2)
    answer.append(max(div1&div2))
    answer.append(min(mul1&mul2))
    return answer