##funções  1 
# Proz Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada.
#  Considera a seguinte definição:

#Soma
#Subtração
#Multiplicação
#Divisão
#Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.


#funcões principais
def soma():
    num1 = float(input("digite o primeiro numero "))
    num2 = float(input("digite o segundo numero"))
    print("Soma: ",num1+num2)

def subtracao():
    num1 = float(input("Digite o primeiro numero :"))
    num2 = float(input("Digite o segundo numero :"))
    print("Subtracao: ",num1-num2)

def multiplicacao():
    num1 = float(input("Digite o primeiro numero :"))
    num2 = float(input("Digite o segundo numero :"))
    print("Multiplicacao: ",num1*num2)

def divisao():
    num1 = float(input("Digite o primeiro numero :"))
    num2 = float(input("Digite o segundo numero : "))
    print("Divisao: ",num1/num2)


opcao=1

#texto de opções para o usuario
print("Digite o número válido para as opções :")

print("0. Sair")
print("1. Somar")
print("2. Subtrair")
print("3. Multiplicação")
print("4. Divisão ")

# aqui usei "while" para trocar o valor da variavel "opcao" de acordo com o numero escolhido pelo usuário
while opcao:
    opcao = int(input("Opção: "))
#
# aqui é onde estou chamando as funçoes principais baseado na escolha do usuário
    if (opcao==1):
        soma()
    elif(opcao == 2):
        subtracao()    
    elif (opcao == 3):
        multiplicacao()
    elif (opcao == 4):
        divisao()     
    else:
        print("Número invalido")       