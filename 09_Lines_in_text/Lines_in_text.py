#!/usr/bin/python3
s=open("file.txt","r+")

print(len(s.readlines()))
s.write("How Are you man ?!")
s.close()
