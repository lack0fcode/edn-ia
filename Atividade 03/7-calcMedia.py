import sys

if len(sys.argv) != 2:
    print("\n-> Instruções:\n     python 7-calcMedia.py <arquivo.txt>\n")
    print("Substitua <arquivo.txt> pelo nome do arquivo contendo quatro notas separadas por espaço.\n")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r') as file:
        line = file.readline().strip()
        parts = line.split()
        if len(parts) != 4:
            raise ValueError("O arquivo deve conter exatamente quatro números.")
        
        notas = []
        for part in parts:
            try:
                nota = float(part)
            except ValueError:
                raise ValueError(f"Valor inválido encontrado: {part}")
            if '.' in part:
                decimal_part = part.split('.')[1]
                if len(decimal_part) > 1:
                    raise ValueError(f"Número com mais de uma casa decimal: {part}")
            if nota < 0:
                raise ValueError(f"Nota negativa encontrada: {nota}")
            if nota > 10:
                raise ValueError(f"Nota maior que 10 encontrada: {nota}")
            notas.append(nota)
        
        n1, n2, n3, n4 = notas
        
        media = (2 * n1 + 3 * n2 + 4 * n3 + 1 * n4) / 10
        
        print(f"\nMedia: {media:.1f}")
        
        if media >= 7.0:
            print("Aluno aprovado.\n")
        elif media < 5.0:
            print("Aluno reprovado.\n")
        else:
            print("Aluno em exame.\n")
            
            while True:
                try:
                    exame = float(input("Digite a nota do exame: "))
                    if exame < 0:
                        print("Nota do exame não pode ser negativa. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("Valor inválido. Digite um número válido.")
            
            nova_media = (media + exame) / 2
            print(f"\nNota do exame: {nova_media:.1f}\n")
            
            if nova_media >= 5.0:
                print("Aluno aprovado em Exame.\n")
            else:
                print("Aluno reprovado em Exame.\n")

except FileNotFoundError:
    print(f"Erro: Arquivo '{filename}' não encontrado.")
except ValueError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
