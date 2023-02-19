def solution(hp):
    answer = 0
    cnt = 0
    while(hp != 0):
        if hp >= 5:
            answer += hp // 5
            hp %= 5
        elif hp >= 3:
            answer += hp // 3
            hp %= 3
        elif hp != 0:
            answer += hp // 1
            hp %= 1
        cnt += 1

    return answer

if __name__ == "__main__":
    print(solution(999))