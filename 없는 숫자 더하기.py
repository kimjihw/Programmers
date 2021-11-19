def solution(numbers):
    answer = -1
    lst = []
    numbers.sort()
    for i in range(10):
        if i not in numbers:
            lst.append(i)
    answer = sum(lst)
    return answer