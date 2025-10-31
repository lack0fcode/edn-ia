import sys

def formato_brl(value: float) -> str:
    return f"R$ {value:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

def calcular_total(salario_fixo: float, vendas: float) -> float:
    comissao = 0.15 * vendas
    return salario_fixo + comissao

def usage():
    print("\nInstruções:\n\n  Comando: python 6-commissionCalc.py <nome-do-arquivo>.txt\n")
    print("Calcula o total a receber de um vendedor com comissão de 15%.\n")
    print("O arquivo deve conter uma linha com: <nome> <salário> <vendas>")
    print("Exemplo: JOAO 1230.30 500.\n")
    print("Use --help ou -h para esta mensagem.\n")

def main() -> None:
    if len(sys.argv) == 1 or (len(sys.argv) > 1 and sys.argv[1] in ['--help', '-h']):
        usage()
        sys.exit(0)
    
    filename = sys.argv[1]
    
    try:
        with open(filename, 'r') as file:
            line = file.readline().strip()
        
        parts = line.split()
        if len(parts) != 3:
            raise ValueError("O Arquivo não tem os campos necessários/corretos.")
        
        nome = parts[0]
        if not nome.isalpha() or len(nome) < 3:
            raise ValueError("Nome inválido: deve ser uma string com pelo menos 3 letras (apenas letras).")
        
        try:
            salario_fixo = float(parts[1])
            if salario_fixo < 0:
                raise ValueError("Salário inválido: deve ser um número positivo.")
        except ValueError:
            raise ValueError("Salário inválido: deve ser um número positivo.")
        
        try:
            vendas = float(parts[2])
            if vendas < 0:
                raise ValueError("Vendas inválidas: devem ser um número positivo.")
        except ValueError:
            raise ValueError("Vendas inválidas: devem ser um número positivo.")
        
        total = calcular_total(salario_fixo, vendas)
        
        print(f"TOTAL = {formato_brl(total)}")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado. Use --help para mais informações.")
    except ValueError as e:
        print(f"Erro: {e}")
        print("Use --help para mais informações.")

if __name__ == "__main__":
    main()
