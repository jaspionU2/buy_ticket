# numberOne = input('digite o primeiro numero: ')
# numberTwo = input('digite o segundo numero: ')

# if numberOne  > numberTwo: 
#     print(f'O numero {numberOne} é maior que o numero {numberTwo}')
# elif numberTwo > numberOne:
#     print(f'O  numero {numberTwo} é maior que o numero {numberOne}')
# else: 
#     print('Os numero digitados são iguais')     

  # -------------------------------------

# number = int(input('digite um numero: '))

# if number > 0: 
#     print(f'o numero {number} é positivo')
# else: 
#     print(f'o numero {number} é negativo')    

   # -------------------------------------
   
noteOne = int(input('digite sua primeira nota: '))
noteTwo = int(input('digite sua segunda nota: '))

gradeAverage = (noteOne + noteTwo) / 2

if gradeAverage == 10:
    print('Aprovado com distinção')
elif gradeAverage >= 7:
    print('Aprovado')
else:
    print('Reprovado')   