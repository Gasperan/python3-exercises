#calculadora hecha en python
firstNumber = input('ingrese el primer numero: ')
secondNumber = input('ingrese el segundo numero: ')
operator = input('ingrese el operador: ')
result = 0

if operator== '*':
	result = int(firstNumber) * int(secondNumber)
elif operator == '+':
	result = int(firstNumber) + int(secondNumber)
elif operator == '-':
	result = int(firstNumber) - int(secondNumber)
else:
	result = int(firstNumber) / int(secondNumber)

print('el resultado es: ' + str(result))