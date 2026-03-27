while True: # Começa o laço infinito
print ("////////////////////////////////")
print ("/ Calculadora /")
num1 =float(input("/ Qual 1º numero / "))
op =str(input("/ Qual a operação / "))
if op == "raiz": resultado = num1 ** 0.5;
else: num2 =float(input("/ Qual 2º numero / "));
#se nao for raiz vai contoinuar o codigo
if op == "+" : resultado = num1 + num2 ;
elif op == "-" : resultado = num1 - num2
elif op == "/" : resultado = num1 / num2
elif op == "*" : resultado = num1 * num2
elif op == "**" : resultado = num1 ** num2
elif op == "=" : resultado = "=? seu burro"
print ("/ ", resultado , " / ")
print ("////////////////////////////////")
continuar = input("Você deseja fazer mais contas? (s/n)")
if continuar != "s":
print("Encerrando a calculadora... Até mais!")
break # Quebra o laço 'while' e finaliza o programa
