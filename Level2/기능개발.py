from collections import OrderedDict
import math

def solution(progresses, speeds):
    answer = []
    lst = []
    for i in range(len(speeds)):
        lst.append(math.ceil((100 - progresses[i]) / speeds[i]))
        if lst[i] < lst[i - 1]:
            lst[i] = lst[i-1]
    cnt = list(OrderedDict.fromkeys(lst))

    for i in cnt:
        answer.append(lst.count(i))
    print(answer)
    return answer

progresses = [93, 30, 55, 90]
speeds = [1, 30, 5, 4]
solution(progresses, speeds)