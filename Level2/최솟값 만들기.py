def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    print(answer)
    return answer

A = [1,2]
B = [3,4]
solution(A, B)