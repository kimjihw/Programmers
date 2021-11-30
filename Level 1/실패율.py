def solution(N, stages):
    answer = {}
    player = len(stages)
    for i in range(1, N + 1):
        if player != 0:
            answer[i] = stages.count(i) / player
            player -= stages.count(i)
        else:
            answer[i] = 0
    print(answer)
    # answer[x]를 찍으면 value 값만 나옴
    answer = sorted(answer, key = lambda x : -answer[x])
    print(answer)
    return answer

N = 5
stages = [2,1,2,6,2,4,3,3]
solution(N, stages)