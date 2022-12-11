def solution(bin1, bin2):
    answer = ''
    convert = int(bin1, 2) + int(bin2, 2)
    answer = str(format(convert, 'b'))

    return answer

bin1 = "10"
bin2 = "11"
solution(bin1, bin2)