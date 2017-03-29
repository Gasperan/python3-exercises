#se importa asi: from { file name } import {class name}
from Calculator import Calculator 

firstNumber = int(input('enter the first number: '))
secondNumber = int(input('enter the second number: '))
operator = input('enter the operator: ')

c = Calculator()

result = 0

if operator== '*':
	result = c.__multiply__(firstNumber,secondNumber)
elif operator == '+':
	result = c.__sum__(firstNumber,secondNumber)
elif operator == '-':
	result = c.__subtract__(firstNumber,secondNumber)
else:
	result = c.__divide__(firstNumber,secondNumber)

print('the result is: ' + str(result))