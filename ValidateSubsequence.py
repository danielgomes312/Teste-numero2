import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        self.assertTrue(program.isValidSubsequence(array, sequence))

# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    # here we have the array first number I think
    rightSide = 0
    # I think that is the last number, but i dont have sure.
    leftSide = 0
    # While the first number is lower them the 
    while rightSide < len(array) and leftSide < len(sequence):
        if array[rightSide] == sequence[leftSide]:
            leftSide +=1
        rightSide +=1
    return leftSide == len(sequence)
    pass
