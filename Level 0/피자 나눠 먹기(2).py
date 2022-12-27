import math

def solution(n):
    answer = 0
    answer = 6 * n / math.gcd(6, n)
    return int(answer / 6)

if __name__ == "__main__":
    print(solution(10))