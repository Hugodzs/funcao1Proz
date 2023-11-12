##funções  1 
# Proz Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada.
#  Considera a seguinte definição:

#Soma
#Subtração
#Multiplicação
#Divisão
#Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.


#funcão principal
def calculator(num1,num2,operador):
    if(operador == 1):
        return num1 + num2
    elif(operador == 2):
        return num1 - num2 
    elif(operador ==3):
        return num1*num2
    elif(operador == 4):
        return num1/num2
    else:
        0               

##texto entrada de dados do usuario para o operador
print("Digite o número válido para as opções :")


print("1. Somar")
print("2. Subtrair")
print("3. Multiplicação")
print("4. Divisão ")

#captura de dados do usuário

operador = int(input("Digite aqui:"))
num1 = int(input("Qual o primeiro número?"))
num2= int(input("Qual segundo numero?"))

# resultado parao usuário
resultado = calculator(num1,num2,operador)

#saida
input(f"Resultado da sua operação é :{resultado}")