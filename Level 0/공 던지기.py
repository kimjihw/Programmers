def solution(numbers, k):
    answer = 0

    throw = 2 * k
    answer = numbers[throw % len(numbers) - 2]
    return answer


solution([1, 2, 3, 4, 5, 6], 5)
