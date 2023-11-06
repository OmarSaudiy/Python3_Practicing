#!/usr/bin/python3

input_string = input("Enter numbers")
list = [int(x) for x in input_string.split()]

s=open("file.txt","r+")
s.write(" ".join(list))