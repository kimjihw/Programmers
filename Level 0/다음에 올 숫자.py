def solution(common):
    answer = 0

    if common[-1] - common[-2] == common[1] - common[0]:
        answer = common[-1] + (common[-1] - common[-2])
    else:
        answer = common[-1] *(common[-1] / common[-2])
    return answer

solution([1, 2, 3, 4])