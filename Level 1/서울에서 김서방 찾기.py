def solution(seoul):
    answer = ''
    kim = ''
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            kim = i

    answer = f'김서방은 {kim}에 있다'
    return answer