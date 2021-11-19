def solution(s, n):
    answer = ''

    for i in s:
        if i.isupper():
            answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
        elif i.islower():
            answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
        elif ord(i) == 32:
            answer += chr(ord(i))
    return answer