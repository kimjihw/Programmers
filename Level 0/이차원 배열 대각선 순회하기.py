def solution(board, k):
    answer = 0
    lst = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:
                lst.append(board[i][j])
    answer = sum(lst)
    return answer

solution([[0, 1, 2],[1, 2, 3],[2, 3, 4],[3, 4, 5]], 2)