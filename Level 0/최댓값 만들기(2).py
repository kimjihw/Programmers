import itertools
import math
from itertools import combinations

def solution(numbers):
    answer = 0
    price = list(itertools.combinations(numbers, 2))
    maximum = []
    for i in range(0, len(price)):
        maximum.append(math.prod(price[i]))
    answer = max(maximum)
    return answer

if __name__ == "__main__":
    print(solution([1, 2, -3, 4, -5]))