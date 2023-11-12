def calculadora():
    while True:
        print("1: Soma\n2: Subtração\n3: Multiplicação\n4: Divisão\n0: Sair")
        opcao = input("Escolha a operação desejada: ")

        if opcao == '0':
            print("Até logo!")
            break
        elif opcao in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                if opcao == '1':
                    resultado = num1 + num2
                    print("Resultado: ", resultado)
                elif opcao == '2':
                    resultado = num1 - num2
                    print("Resultado: ", resultado)
                elif opcao == '3':
                    resultado = num1 * num2
                    print("Resultado: ", resultado)
                elif opcao == '4':
                    if num2 != 0:
                        resultado = num1 / num2
                        print("Resultado: ", resultado)
                    else:
                        print("Não é possível dividir por zero.")
            except ValueError:
                print("Por favor, insira números válidos.")
        else:
            print("Essa opção não existe. Escolha novamente.")

calculadora()
