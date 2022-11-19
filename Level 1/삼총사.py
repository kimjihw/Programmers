
from itertools import combinations

def solution(number):
    answer = 0
    lst = tuple(combinations((number), 3))
    for i in lst:
        if sum(i) == 0:
            answer += 1

    return answer

numbers = [-2, 3, 0, 2, -5]
solution(numbers)