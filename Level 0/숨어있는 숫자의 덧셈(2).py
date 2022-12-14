def solution(my_string):
    answer = 0
    ans = []
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, " ")
    my_string = my_string.strip()
    for i in my_string.split(" "):
        if i.isdecimal():
            ans.append(int(i))
    answer = sum(ans)

    return answer

my_string = "aAb1B2cC34oOp"
solution(my_string)