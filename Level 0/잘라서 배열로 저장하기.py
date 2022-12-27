def solution(my_str: str, n: int) -> list:
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(my_str[i : i + n])
    return answer


if __name__ == "__main__":
    print(solution("abc1Addfggg4556b", 6))
