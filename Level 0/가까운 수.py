def solution(array: list, n: int) -> int:
    answer = 0
    minus = []
    min_lst = []
    for i in array:
        minus.append(abs(n - i))
    min_num = min(minus)
    num_index = [i for i, x in enumerate(minus) if x == min_num]
    for i in num_index:
        min_lst.append(array[i])

    answer = min(min_lst)

    return answer


if __name__ == "__main__":
    print(solution([10, -10, 12], 0))
