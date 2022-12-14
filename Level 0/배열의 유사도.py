def solution(s1, s2):
    answer = 0
    for i in s1:
        for j in s2:
            if i == j:
                answer += 1
    return answer

s1 = ["a", "b", "c"]
s2 = ["com", "b", "d", "p", "c"]
solution(s1, s2)