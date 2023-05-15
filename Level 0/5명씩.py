def solution(names):
    answer = []
    for i in range(len(names)):
        if i % 5 == 0:
            answer.append(names[i])

    return answer

solution(["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"])