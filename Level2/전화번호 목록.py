from itertools import combinations

def solution(phone_book):
    answer = True
    num = list(combinations(phone_book, 2))
    for i in range(len(num)):
        if num[i][0] in num[i][1]:
            answer = False
            break
    print(num)
    print(answer)
    return answer

phone_book = ["119", "97674223", "1195524421"]
solution(phone_book)