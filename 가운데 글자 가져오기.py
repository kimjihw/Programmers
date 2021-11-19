def solution(s):
    answer = ''
    cnt = 0
    if len(s) % 2 == 0:
        cnt = int(len(s) / 2) - 1
        answer = s[cnt:cnt + 2]
    else:
        cnt = int((len(s) - 1) / 2)
        answer = s[cnt]

    return answer