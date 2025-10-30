import sys

def instrucoes():
    print("\nInstruções: forneça 2 inteiros via stdin.\nExemplo:")
    print("  echo \"10 20\" | python 5-UEsomaCalc.py\n")

def main():
    interactive = sys.stdin.isatty()

    if interactive:
        instrucoes()
        try:
            line = input("Digite 2 inteiros (separados por espaço ou Enter): ")
        except EOFError:
            print("Erro: entrada não fornecida.", file=sys.stderr)
            sys.exit(1)

        tokens = line.strip().split()
    else:
        tokens = sys.stdin.read().strip().split()
        if not tokens:
            print("\nErro: entrada vazia. Forneça 2 inteiros via stdin.", file=sys.stderr)
            instrucoes()
            sys.exit(1)

    if len(tokens) < 2:
        print("\nErro: entrada insuficiente. Forneça 2 inteiros.\n\n", file=sys.stderr)
        sys.exit(1)

    try:
        A = int(tokens[0])
        B = int(tokens[1])
    except ValueError:
        print("Erro: entrada inválida — todos os valores devem ser numeros inteiros.", file=sys.stderr)
        sys.exit(1)

    X = A + B
    print(f"X = {X}")

if __name__ == "__main__":
    main()