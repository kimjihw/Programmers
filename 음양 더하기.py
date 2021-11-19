def solution(absolutes, signs):
    answer = 123456789

    for i in range(len(absolutes)):
        if signs[i] == True:
            continue
        else:
            absolutes[i] -= absolutes[i] * 2

    answer = sum(absolutes)
    return answer