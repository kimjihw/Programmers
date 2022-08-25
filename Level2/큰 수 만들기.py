def solution(number, k):
    answer = []

    for i in number:
        while k > 0 and answer and answer[-1] < i:
            answer.pop()
            k -= 1
        answer.append(i)
    return "".join(answer[:len(answer) - k]) # 여기 부분이 777777, 2 일경우엔 K값도 2 그대로고 answer값도 그대로라서 길이를 잘라주는 것

number = "77777777"
k = 2

solution(number, k)