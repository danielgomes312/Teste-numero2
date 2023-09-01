# O(n^2) time | O(1) space
array = [3, 5, -4, 8, 11, 1, -1, 6]

targetSum = 10

from tkinter import *
import datetime
import time
import winsound
from threading import *

def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum =array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return[]

twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)

# O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentiontialMatch = targetSum - num
        if targetSum - num in nums:
            return [targetSum - num, num]
        else:
            nums[num] = True
    return []