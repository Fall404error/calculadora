while True:  # Começa o laço infinito
    print("/////////////////////////////////////////////////")
    print("/                  Calculadora                  /")
    
    try:
        num1 = float(input("/                Qual 1º número?                / "))
    except ValueError:
        print("Erro: Por favor, insira um número válido.")
        continue  # Se o valor não for um número, o programa volta para o início
    
    op = input("/    Qual a operação? (+, -, *, /, **, raiz)    / ").strip().lower()  # Tornar a operação mais flexível
    
    # Se a operação for raiz quadrada
    if op == "raiz":
        resultado = num1 ** 0.5  # Raiz quadrada do número
    else:
        try:
            num2 = float(input("/                Qual 2º número?                /" ))  # Pergunta o segundo número
        except ValueError:
            print("Erro: Por favor, insira um número válido.")
            continue  # Se o valor não for um número, o programa volta para o início
        
        # Operações básicas
        if op == "+":
            resultado = num1 + num2
        elif op == "-":
            resultado = num1 - num2
        elif op == "/":
            if num2 == 0:  # Prevenir divisão por zero
                resultado = "Erro: divisão por zero"
            else:
                resultado = num1 / num2
        elif op == "*":
            resultado = num1 * num2
        elif op == "**":
            resultado = num1 ** num2
        else:
            resultado = "Operação inválida"
    
    print("/      Resultado: ", resultado, "                       /")
    print("/////////////////////////////////////////////////")
    
    continuar = input("Você deseja fazer mais contas? (s/n) ").strip().lower()
    if continuar != "s":
        print("Encerrando a calculadora... Até mais!")
        break  # Quebra o laço 'while' e finaliza o programa