import math

def calculator():
    print("Calculadora Científica")
    print("Escolha a operação:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Exponenciação (**)")
    print("6. Raiz Quadrada (sqrt)")
    print("7. Seno (sin)")
    print("8. Cosseno (cos)")
    print("9. Tangente (tan)")
    print("10. Logaritmo (log)")
    print("11. Sair")

    while True:
        try:
            choice = input("\nDigite o número da operação desejada: ")

            if choice == '11':
                print("Encerrando a calculadora. Até logo!")
                break

            if choice in ['1', '2', '3', '4', '5']:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if choice == '1':
                    print(f"Resultado: {num1 + num2}")
                elif choice == '2':
                    print(f"Resultado: {num1 - num2}")
                elif choice == '3':
                    print(f"Resultado: {num1 * num2}")
                elif choice == '4':
                    if num2 != 0:
                        print(f"Resultado: {num1 / num2}")
                    else:
                        print("Erro: Divisão por zero não é permitida.")
                elif choice == '5':
                    print(f"Resultado: {num1 ** num2}")

            elif choice == '6':
                num = float(input("Digite o número: "))
                if num >= 0:
                    print(f"Resultado: {math.sqrt(num)}")
                else:
                    print("Erro: Não é possível calcular a raiz quadrada de um número negativo.")

            elif choice in ['7', '8', '9']:
                num = float(input("Digite o ângulo em graus: "))
                radians = math.radians(num)

                if choice == '7':
                    print(f"Resultado: {math.sin(radians)}")
                elif choice == '8':
                    print(f"Resultado: {math.cos(radians)}")
                elif choice == '9':
                    print(f"Resultado: {math.tan(radians)}")

            elif choice == '10':
                num = float(input("Digite o número: "))
                if num > 0:
                    print(f"Resultado: {math.log(num)}")
                else:
                    print("Erro: Logaritmo de número não positivo não é definido.")

            else:
                print("Escolha inválida. Por favor, tente novamente.")

        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número válido.")

if __name__ == "__main__":
    calculator()

