def solution(nums):
    answer = 0
    mon = len(nums)/2

    nums = set(nums)
    if mon < len(nums):
        answer = int(mon)
    else:
        answer = int(len(nums))

    print(int(answer))
    return answer

nums = [3,1,2,3]
solution(nums)