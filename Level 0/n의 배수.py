def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)
    return answer

n = 3
numlist = [4, 5, 6, 7, 8, 9, 10, 11, 12]

solution(n, numlist)