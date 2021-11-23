import re

def solution(new_id):
    answer = ''
    lst = []

    new_id = new_id.lower()
    new_id = re.sub('[^0-9a-z_.-]+', '', new_id)
    new_id = re.sub('\.+','.', new_id)
    answer = new_id.strip('.')
    if answer == "":
        answer = "a"
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.rstrip(".")
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]
    return answer