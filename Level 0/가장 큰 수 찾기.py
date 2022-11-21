def solution(array):
    answer = []
    answer.append(max(array))
    answer.append(array.index(max(array)))
    return answer

answer = [1, 8, 3]
solution(answer)