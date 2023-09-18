def solution(score):
    lst = []
    for i in score:
        lst.append(sum(i))
    rank = [sorted(lst, reverse=True).index(s) + 1 for s in lst]

    return rank
