print('\n ********* Calculadora Pyhton *********\n ')

#Funções para operações
def som(num1,num2):
    return  num1 + num2


def sub(num1,num2):
    return num1 - num2

def div(num1,num2):
    if num2 == 0:
        raise ('Não é possivel dividir por zero')
    return num1 / num2

def mult(num1,num2):
    return num1 * num2

#Perguntar operação
op = input('Escolha o número referente a operação \n1 - Soma \n2 - Subtração \n3- Divisão\n4- Multiplicação ' )

#Numeros
num1 = float(input('Qual o primeiro número?: '))
num2 = float(input('Qual o segundo número?'))

#Condição relacionando resposta a função operação
if op == '1':
    Result = som(num1,num2)
    print(Result)
elif op == '2':
    Result = sub(num1,num2)
    print(Result)
elif op == '3':
    Result = div(num1,num2)
    print(Result)
elif op == '4':
    Result = mult(num1,num2)
    print(Result)
else:
    print('Escolha umas das 4 opções')



#Printar Resultado
print('Esta parte fiz depois')
