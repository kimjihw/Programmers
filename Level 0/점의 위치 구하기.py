def solution(dot: list) -> int:
    answer = 0
    if dot[0] < 0 < dot[1]:
        return 2
    if dot[0] > 0 and dot[1] > 0:
        return 1
    if dot[0] > 0 > dot[1]:
        return 4
    if dot[0] < 0 and dot[1] < 0:
        return 3
    return answer


if __name__ == "__main__":
    print(solution([3, -2]))
