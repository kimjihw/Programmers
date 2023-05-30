import itertools
import math


def solution(nums):
    answer = 0

    prime_number = []

    combi = list(itertools.combinations(nums, 3))

    for i in range(len(combi)):
        prime_number.append(sum(combi[i]))

        isPrime(prime_number[i])
    return answer

def isPrime(x):

    m = int(x ** 0.5)

nums = [1,2,7,6,4]
solution(nums)