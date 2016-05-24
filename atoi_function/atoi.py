import sys

def my_atoi(string):

    integer = 0
    sign = 1

    for i in range(len(string)):
        character = string[i]
        
        if character == "+":
            continue
        elif character == "-":
            sign = -1
            continue
            

        # Multiply number so far by 10 to shift digits to the left. Add latest digit.
        integer = integer*10 + (ord(character) - ord('0'))

    return integer * sign


test_string = "-123"

print my_atoi(test_string)
