#!/usr/bin/env python3

# Created by: Ryan Chung Kam Chung
# Created on: January 2021
# This program converts grades to percents


def input_to_percent(grade):
    # Takes the grade input and returns the percent equivalent

    if grade == "R":
        percent = 30
    elif grade == "1-":
        percent = 51
    elif grade == "1":
        percent = 55
    elif grade == "1+":
        percent = 58
    elif grade == "2-":
        percent = 61
    elif grade == "2":
        percent = 65
    elif grade == "2+":
        percent = 68
    elif grade == "3-":
        percent = 71
    elif grade == "3":
        percent = 75
    elif grade == "3+":
        percent = 78
    elif grade == "4-":
        percent = 83
    elif grade == "4":
        percent = 90
    elif grade == "4+":
        percent = 97
    else:
        percent = -1

    return percent


def main():
    # Takes a grade input and outputs the percentage equivalent

    while True:
        # Input
        grade = input("Enter grade: ")

        # Process
        percent_grade = input_to_percent(grade)

        if percent_grade == -1:
            print("Invalid input")
            print(" ")
            continue

        break

    # Output
    print("Your grade in percent is: {}%".format(percent_grade))


if __name__ == "__main__":
    main()
