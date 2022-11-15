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
        return True;
    print("Divisor não pode ser zero.")
    return False;


def sqr_root(x):
    if x >= 0:
        print("Raiz quadrada de ", x, " = ", math.sqrt(x))
        return True;
    print("Impossível de realizar uma raiz quadrada de um número negativo.")
    return False;


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
            x = float(input("Introduza o primeiro número - "))
            sqr_root(x)
        elif 5 >= userChoice >= 0:
            while True:
                x = input("Introduza o primeiro número - ")
                y = input("Introduza o segundo número - ")
                if x.isnumeric() and y.isnumeric():
                    x = float(x)
                    y = float(y)
                    break;
                print("Valores inválidos. Re-introduza os valores.")

            match userChoice:
                case 1:
                    add(x, y)
                case 2:
                    subtract(x, y)
                case 3:
                    multiply(x, y)
                case 4:
                    divide(x, y)
                case 5:
                    percentage(x, y)

        else:
            print("Opção inválida")

        repeat = input("Deseja realizar outra operação? \n 1 - Sim \n 2 - Não \n")
        if input == 2:
            break
    else:
        print("Escolha inválida")
