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
    else:
        print("Divisor não pode ser zero.")


def sqr_root(x):
    if x >= 0:
        print("Raiz quadrada de ", x, " = ", math.sqrt(x))
    else:
        print("Impossível de realizar uma raiz quadrada de um número negativo.")


def percentage(part, full):
    print(part, " é ", (part / full) * 100, "% de ", full)


print("--PROGRAMA DE CALCULADORA--")
while True:
    print("Seleciona uma operação :")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Percentagem")
    print("6 - Raiz Quadrada")

    userChoice = input()

    if userChoice.isnumeric():
        userChoice = int(userChoice)
        if userChoice == 6:
            while True:
                input_x = input("Introduza o primeiro número - ").strip()
                if input_x.isnumeric():
                    input_x = float(input_x)
                    sqr_root(input_x)
                    break
                print("Valor inválido. Re-introduza o valor.")
        elif 5 >= userChoice >= 0:
            while True:
                input_x = input("Introduza o primeiro número - ").strip()
                input_y = input("Introduza o segundo número - ").strip()
                if input_x.isnumeric() and input_y.isnumeric():
                    input_x = float(input_x)
                    input_y = float(input_y)
                    break
                print("Valores inválidos. Re-introduza os valores.")

            match userChoice:
                case 1:
                    add(input_x, input_y)
                case 2:
                    subtract(input_x, input_y)
                case 3:
                    multiply(input_x, input_y)
                case 4:
                    divide(input_x, input_y)
                case 5:
                    percentage(input_x, input_y)

        else:
            print("Opção inválida")

        repeat = input("Deseja realizar outra operação? \n 1 - Sim \n 2 - Não \n")
        if repeat == "2":
            break
    else:
        print("Escolha inválida")
