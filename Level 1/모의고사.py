def solution(answers):
    answer = []
    cnt1, cnt2, cnt3 = 0, 0, 0
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]

    for i in range(len(answers)):
        # 길이별로 나머지크기 나눠줌으로써 시간 절약
        s1 = i % 5
        s2 = i % 8
        s3 = i % 10
        
        if(num1[s1] == answers[i]):
            cnt1 += 1
        if (num2[s2] == answers[i]):
            cnt2 += 1
        if (num3[s3] == answers[i]):
            cnt3 += 1

    max_num = max(cnt1, cnt2, cnt3)

    if (max_num == cnt1):
        answer.append(1)
    if (max_num == cnt2):
        answer.append(2)
    if (max_num == cnt3):
        answer.append(3)

    print(answer)
    return answer

answers = [1,3,2,4,2]
solution(answers)