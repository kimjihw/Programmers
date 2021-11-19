def solution(n):
    answer = 0
    rev_base = ''
    while n > 0: # 10진수에서 n진수로 변환 알고리즘
        n, mod = divmod(n, 3)
        rev_base += str(mod)
    rev_base = list(rev_base[::-1])
    for i in range(len(rev_base)):
        answer += (int(rev_base[i]) * (3**i))
    return answer