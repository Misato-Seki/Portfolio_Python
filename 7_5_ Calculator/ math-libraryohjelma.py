import math
print('Calculator')
number_1 = int(input('Give the first number: '))
number_2 = int(input('Give the second number: '))
while True:			   
    print('(1) +')
    print('(2) -')
    print('(3) *')
    print('(4) /')
    print('(5)sin(number1/number2)')
    print('(6)cos(number1/number2)')
    print("(7)Change numbers")
    print("(8)Quit")
    print("Current numbers: ",number_1,number_2)
    mark = int(input('Please select something (1-6): '))

    if mark == 1:
	    print('The result is: ',number_1 + number_2)
    elif mark == 2:
	    print('The result is: ',number_1 - number_2)
    elif mark == 3:
	    print('The result is: ',number_1 * number_2)
    elif mark == 4:
	    print('The result is: ',number_1 / number_2)
    elif mark == 5:
	    print('The result is: ',math.sin(number_1 / number_2))
    elif mark == 6:
	    print('The result is: ',math.cos(number_1 / number_2))
    elif mark == 7:
        number_1 = int(input("Give the first number:"))
        number_2 = int(input("Give the second number:"))
    else:
        break
print("Thank you!")
