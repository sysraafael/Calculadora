#Calculadora Simples

def menssagem(): #Menssagem Inicial
    print("=================================")
    print("========== CALCULADORA ==========")
    print("=================================")

def menssagem1(): # Menssagem Das Operações
    print("--> Soma : +")
    print("--> subtração: -")
    print("--> Multiplicação: *")
    print("--> divisão: /")

menssagem()

valor1 = int(input("Informe o primero número: "))
valor2 = int(input("Informe o segundo número: "))

menssagem1()

operacao = input("Informe a Operação com os sinais a cima: ")

resultado = 0

#Fazendo Operação

if(operacao == '+'):
  resultado = valor1 + valor2
elif(operacao == '-'):
  resultado = valor1 - valor2
elif(operacao == '*'):
  resultado = valor1 * valor2
elif(operacao == '/'):
  resultado = valor1 / valor2
else:
  print(":( Houve algum ERRO!!! Reinicie o programa.")
  
print("O resultado é: ",valor1,operacao,valor2,'=',resultado)