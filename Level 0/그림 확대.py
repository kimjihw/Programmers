def solution(picture, k):
    answer = []
    for i in picture:
        s = ""
        for j in i:
            s += j * k
        for i in range(k):
            answer.append(s)
    return answer

solution([".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."], 2)