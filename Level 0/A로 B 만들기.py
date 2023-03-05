from collections import Counter

def solution(before, after):
    answer = 0
    blst = (Counter(before))
    alst = (Counter(after))

    if alst == blst:
        answer = 1
    else:
        answer = 0
    return answer

solution("olleh", "hello")