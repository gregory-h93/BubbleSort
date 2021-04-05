def bubbleSort(array, arraySize):
    for maxElement in range(arraySize - 1, 0 - 1, -1):
        for index in range(0, maxElement - 1 + 1, 1):
            if array[index] > array[index + 1]:
                temp = array[index]
                array[index] = array[index + 1]
                array[index + 1] = temp

def getNumbers(array, arraySize):
    num1 = 0
    for index in range(0, arraySize - 1 + 1, 1):
        print("Enter number " + str((index + 1)))
        array[index] = int(input())

def showNumbers(array, arraySize):
    for index in range(0, arraySize - 1 + 1, 1):
        print(array[index])

def swap(a, b):
    temp = a
    a = b
    b = temp

# Main
num1 = 0
size = 10
numbers = [0] * (size)

# Calls the assorted modules to enter the numbers and sort them
getNumbers(numbers, size)
bubbleSort(numbers, size)
print("Here are the numbers sorted from lowest to highest:")

# Module to display the numbers as sorted.
showNumbers(numbers, size)
