import sys
import math
import re

pi = 3.14159265

def instrucoes():
    print("Instruções:\n python 1-areaCirc.py <raio>\n Ou: echo <raio> | python 1-areaCirc.py\n")
    print("Exemplos:\n python 1-areaCirc.py 2.00\n echo 2.00 | python 1-areaCirc.py\n")
    print("Nota: O raio deve ser fornecido com pelo menos duas casas decimais (ex: 2.00).")

def precisao(s):
    pattern = r'^-?\d+\.\d{2,}$'
    return re.match(pattern, s.strip()) is not None

def main():
    data = ""
    if not sys.stdin.isatty():
        data = sys.stdin.read().strip()

    if not data and len(sys.argv) == 1:
        instrucoes()
        return

    if not data and len(sys.argv) > 1:
        data = sys.argv[1]

    raio_str = data.split()[0]

    if not precisao(raio_str):
        print("Erro: o raio deve ser fornecido com pelo menos duas casas decimais (ex: 2.00).")
        return

    try:
        raio = float(raio_str)
    except Exception:
        print("Erro: entrada inválida. Forneça um número real para o raio.")
        return

    if raio < 0:
        print("Erro: o raio não pode ser negativo.")
        return

    area = pi * math.pow(raio, 2)
    print(f"A={area:.4f}")

if __name__ == "__main__":
    main()