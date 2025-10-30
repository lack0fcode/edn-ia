import sys

def instrucoes():
	print("\nInstruções: forneça o número do funcionário, horas trabalhadas e valor por hora.\nExemplo:")
	print('  echo "25 100 5.50" | python 6-calculaSalario.py')

def main():
	interactive = sys.stdin.isatty()

	if interactive:
		instrucoes()
		try:
			line = input("Digite os valores (separados por espaço): ")
		except EOFError:
			print("Erro: entrada não fornecida.", file=sys.stderr)
			sys.exit(1)

		tokens = line.strip().split()
	else:
		tokens = sys.stdin.read().strip().split()
		if not tokens:
			print("\nErro: entrada vazia. Forneça 3 valores via stdin.", file=sys.stderr)
			instrucoes()
			sys.exit(1)

	if len(tokens) < 3:
		print("\nERRO: entrada insuficiente. Forneça 3 valores.", file=sys.stderr)
		sys.exit(1)

	try:
		numero_funcionario = int(tokens[0])
		horas_trabalhadas = int(tokens[1])
		valor_por_hora = float(tokens[2])
	except ValueError:
		print("ERRO: entrada inválida. Os dois primeiros valores devem ser inteiros e o terceiro um número (float).", file=sys.stderr)
		sys.exit(1)

	salario = horas_trabalhadas * valor_por_hora
	print(f"Número do Funcionário = {numero_funcionario}")
	print(f"Salário = R$ {salario:.2f}")

if __name__ == "__main__":
	main()