from numpyencoder import NumpyEncoder
import numpy as np

def solution(arr1, arr2):
    answer = [[]]
    answer = np.matmul(arr1, arr2)
    print(answer)
    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
solution(arr1, arr2)