#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    k=0
    for i in range(0,len(grades)):
        g=grades[i]%10
        k=0
        
        #diff with nearest multiple of 5 
        
        if(g<5):
            k=5-g
        else:
            k=10-g

        #rounding off

        if(k>3 or k==3 or grades[i]<38):
            continue
        else:
            grades[i]=grades[i]+k
    return(grades)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
