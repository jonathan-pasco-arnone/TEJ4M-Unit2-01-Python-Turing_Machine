#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: February 2022
# This is the turing machine that prints the
# binary values of 11 to 16

import time

# Pauses the program
def pause(seconds):
    time.sleep(seconds)

# Prints all the digits
def output(numberList):
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
    # This function holds the main turing machine
    numberList = [1,0,1,1]
    # makes the index the same as the last digit in 
    index = len(numberList) - 1
    currentNumber = 12
    
    print("11 in binary is ", end = '')
    output(numberList)

    # The rules that will repeat over and over
    while True:

        # If the index is one to the left out of bounds,
        # then set the index to 0 and place a new value
        # there to make it in bounds.
        if index == -1:
            index = moveLeft(index)
            numberList = insert(numberList, index, 1)
            break

        # If the location is a 0
        if numberList[index] == 0:
            numberList = erase(numberList, index)
            numberList = insert(numberList, index, 1)
            
            print("\n"
                + str(currentNumber)
                + " in binary is ", end='')
            output(numberList)
            currentNumber = currentNumber + 1

            pause(2.5)

            # Moves tape left until at the furthest number
            while index < (len(numberList) - 1):
                index = moveLeft(index)

        # If the location is a 1
        elif numberList[index] == 1:
            numberList = erase(numberList, index)
            numberList = insert(numberList, index, 0)
            index = moveRight(index)

    print("\n16 in binary is ", end="")
    output(numberList)
    
    print("\n\nDone.")

if __name__ == "__main__":
    main()
