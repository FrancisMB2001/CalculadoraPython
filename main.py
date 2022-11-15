import math


def add(x, y):
    print(x, " + ", y, " = ", (x + y))


def subtract(x, y):
    print(x, " - ", y, " = ", (x - y))


def multiply(x, y):
    print(x, " * ", y, " = ", (x * y))


def divide(x, y):
    if y != 0:
        print(x, " / ", y, " = ", (x / y))
    print("Divisor não pode ser zero.")


def sqr_root(x):
    if x >= 0:
        print("Raiz quadrada de ", x, " = ", math.sqrt(x))
    print("Impossível de realizar uma raiz quadrada de um número negativo.")


def percentage(part, full):
    print(part, " é ", (part / full) * 100, " % de ", full)


print("--PROGRAMA DE CALCULADORA--")
while True:
    print("Seleciona uma operação :")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Percentagem")
    print("6 - Raiz Quadrada")
    print("0 - Limpar Ecrã")

    userChoice = input()

    if userChoice.isnumeric():
        userChoice = int(userChoice)
        if userChoice == 6:
            x = float(input("Introduza o primeiro número - "))
            sqr_root(x)
        elif userChoice <= 5 or userChoice >= 0:
            x = float(input("Introduza o primeiro número - "))
            y = float(input("Introduza o segundo número - "))

            match userChoice:
                case '1':
                    add(x, y)
                case '2':

            if userChoice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
        else:
            print("Opção inválida")

            repeat = input("Deseja realizar outra operação? \n 1 - Sim \n 2 - Não")
            if input == 2:
                break
    else:
        print("Escolha inválida")

