import sys
import os

if len(sys.argv) > 1:
    print("\nEste programa não aceita argumentos.\nExecute apenas 'python 1-fullCalc.py'.\n")
    sys.exit(1)

if not sys.stdin.isatty() and os.environ.get('TESTING') != '1':
    print("\nEste programa deve ser executado interativamente com 'python 1-fullCalc.py'.\n")
    sys.exit(1)

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
    except ValueError:
        print("\nEntrada inválida. Digite um número válido.\n")
        continue

    try:
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("\nEntrada inválida. Digite um número válido.\n")
        continue

    op = input("Digite a operação (+, -, *, /): ")

    if op not in ['+', '-', '*', '/']:
        print("\nOperação inválida. Use +, -, *, ou /.\n")
        continue

    try:
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2
        result += 0.0  
        print(f"Resultado: {result:.2f}\n")
        break
    except ZeroDivisionError:
        print("\nErro: Divisão por zero não é permitida.\n")
        continue
