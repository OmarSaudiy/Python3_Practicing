# Author: Omar Ahmed Hassan             #
#                                       #
# Date  : 4 Oct, 2023                   #
#                                       #
# Description : 01_Count_4s_in_list     #

#!/usr/bin/python3

x=list(input("Enter List of a single digit elements:"))

y = 0
for i in range(0,len(x),1) :
    if x[i] == '4' :
        y+=1
    else:
        pass

print(f"4 is found :{y} times ")