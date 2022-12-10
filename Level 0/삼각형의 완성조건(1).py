def solution(sides):
    answer = 0
    maxItem = max(sides)
    sides.remove(maxItem)
    if maxItem < sum(sides):
        answer = 1
    else:
        answer = 2
    print(answer)
    return answer

sides = [3, 6, 2]
solution(sides)