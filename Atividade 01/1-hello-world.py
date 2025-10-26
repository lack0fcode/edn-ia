import sys

def main(name: str = "world") -> None:
    print(f"Hello, {name}!")

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    main(name)

# Caso o usuario execute o script passando um nome como argumento
# na linha de comando, ele sera saudado por esse nome.
# Exemplo:  python 1-hello-world.py Rafael
# Saida:    Hello, Rafael!