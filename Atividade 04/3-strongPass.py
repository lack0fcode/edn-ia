import sys

if len(sys.argv) == 1:
    if not sys.stdin.isatty():
        print("Entrada aceita.\n     Ajuda: python 3-strongPass.py --help")
    else:
        while True:
            senha = input("Digite uma senha (ou 'sair' para encerrar): ")
            if senha.lower() == 'sair':
                print("Programa encerrado.")
                break
            if len(senha) >= 8 and any(char.isdigit() for char in senha):
                print("Senha forte aceita!")
                break
            else:
                print("Senha fraca. Deve ter pelo menos 8 caracteres e conter pelo menos um número.")
elif len(sys.argv) == 2 and sys.argv[1] == '--help':
    print("""\nUso: python 3-strongPass.py [--help]

Verifica se uma senha é forte.

Requisitos para senha forte:
  - Pelo menos 8 caracteres
  - Pelo menos um número

O programa pede senhas interativamente até que uma válida seja inserida ou 'sair' seja digitado.\n""")
else:
    print("Argumento inválido. Use --help para instruções.\n")
