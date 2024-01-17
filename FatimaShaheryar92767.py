#Fatima Shaheryar 92767
#BanoQabil Python Midterm
#Calculator
a="y"
while a=='y' or a=='Y':
    print('This program will function as a calculator.')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Power')
    x=input('Choose an operator 1,2,3,4 or 5: ')
    print('Remember: The order in which you input numbers is the order in which operations will be executed.')
    num1=int(input('Enter the first number  '))
    num2=int(input('Enter the second number  '))
    if x=='1':
        print(num1+num2)
    elif x=='2':
        print(num1-num2)
    elif x=='3':
        print(num1*num2)
    elif x=='4':
        print(num1/num2)
    elif x=='5':
        print(num1**num2)
    else:
        print('Not a valid Operator. Enter from (1,2,3,4,5)')
    a=input('Do you want to continue(Y/N): ')
print('Either enter Y or N')
