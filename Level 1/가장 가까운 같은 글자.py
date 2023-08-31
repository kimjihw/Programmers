def solution(s):
    answer = []
    stack = ""

    for i in range(len(s)):
        if s[i] in stack:
            answer.append(i - stack.rindex(s[i]))
        else:
            answer.append(-1)
        stack += s[i]

    return answer


solution("banana")
