import sys

if len(sys.argv) > 1:
    if sys.argv[1] == '--help':
        print("Este programa permite registrar notas de uma turma.")
        print("Execute sem argumentos para iniciar o registro de notas.")
        print("Digite notas válidas (0 a 10) ou 'fim' para terminar.")
        print("Notas inválidas serão ignoradas.")
        print("No final, será exibida a média da turma.")
    else:
        print("Uso: python 2-media_infinita.py [--help]")
else:
    notas = []
    while True:
        entrada = input("Digite uma nota (0-10) ou 'fim' para terminar: ")
        if entrada.lower() == 'fim':
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Deve ser entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número ou 'fim'.")
    
    if notas:
        media = sum(notas) / len(notas)
        print(f"\nMédia da turma: {media:.2f}\n")
    else:
        print("Nenhuma nota válida foi registrada.")
