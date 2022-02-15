#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: February 2022
# This is the turing machine that prints each
# binary value from 1 to 10

def output(numberList):
    # Prints all the digits
    for number in numberList:
        print(str(number), end = '')

# Inserts an inputted number in the inputted index
def insert(numberList, index, insertingNumber):
    numberList.insert(index, insertingNumber)
    return numberList

# Erases the current index
def erase(numberList, index):
    numberList.pop(index)
    return numberList

# Moves the tape to the right once
def moveRight(index):
    index = index - 1
    return index

# Moves the tape to the left once
def moveLeft(index):
    index = index + 1
    return index

# All the commands
def main():
    tenBinary = [1,0,1,0]
    # This function holds the main turing machine
    numberList = []
    # makes the index the same as the last digit in 
    index = len(numberList) - 1
    # Which binary number we are on
    currentNumber = 1

    # The rules that will repeat over and over
    while True:

        # If the index is one to the left out of bounds,
        # then set the index to 0 and place a new value
        # there to make it in bounds.
        if index == -1:
            index = 0
            numberList = insert(numberList, index, 0)

        # If the location is a 0
        if numberList[index] == 0:
            numberList = erase(numberList, index)
            numberList = insert(numberList, index, 1)
            print("\n" + str(currentNumber) + " in binary is ", end='')
            output(numberList)
            currentNumber = currentNumber + 1

            # Moves tape left until at the furthest number
            while index < (len(numberList) - 1):
                index = moveLeft(index)

        # If the location is a 1
        elif numberList[index] == 1:
            numberList = erase(numberList, index)
            numberList = insert(numberList, index, 0)
            index = moveRight(index)

        # If the list is currently on ten in binary
        if numberList == tenBinary:
            break
    
    print("\n\nDone.")

if __name__ == "__main__":
    main()