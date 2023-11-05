#!/usr/bin/python3


input_string = input("Enter numbers")
number_list = [int(x) for x in input_string.split()]

number_list.sort()
print(number_list[-1])