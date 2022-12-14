def solution(my_string):
    answer = 0
    lst = []
    for i in my_string:
        if(i.isdecimal()):
            lst.append(int(i))
    answer = sum(lst)

    return answer

my_string = "aAb1B2cC34oOp"
solution(my_string)