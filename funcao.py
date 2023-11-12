##funcao1Proz Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:

#Soma
#Subtração
#Multiplicação
#Divisão
#Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.


#funcao principal
def soma():
    x = float(input("digite o primeiro numero "))
    y = float(input("digite o segundo numero"))
    print("Soma: ",x+y)

def subtracao():
    x = float(input("digite o primeiro numero "))
    y = float(input("digite o segundo numero "))
    print("Subtracao: ",x-y)

def multiplicacao():
    x = float(input("digite o primeiro numero "))
    y = float(input("digite o segundo numero "))
    print("Multiplicacao: ",x*y)

def divisao():
    num1 = float(input("digite o primeiro numero "))
    num2 = float(input("digite o segundo numero "))
    print("Divisao: ",x/y)


soma()