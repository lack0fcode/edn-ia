import sys

def imcValor(imc: float) -> str:
	if imc < 18.5:
		return "Abaixo do peso"
	if imc < 25:
		return "Peso normal"
	if imc < 30:
		return "Sobrepeso"
	return "Obeso"

def parse_number(s: str) -> float:
	return float(s.replace(',', '.'))

def prompt_float(name: str, prompt: str, min_value: float, max_value: float):
	while True:
		try:
			s = input(prompt).strip()
		except EOFError:
			print("\nEntrada encerrada pelo usuário. Saindo.")
			return None
		if not s:
			print(f"{name.capitalize()} vazio. Digite um número (ex: 70 ou 1,75).")
			continue
		try:
			val = parse_number(s)
		except ValueError:
			print(f"Entrada inválida para {name}: '{s}'.\nUse um número (ex: 70 ou 70,0 para peso; 1.75 ou 1,75 para altura).")
			continue
		if val <= 0:
			print(f"Valor inválido ({val}).\n{name.capitalize()} deve ser maior que zero.")
			continue
		if val > max_value:
			print(f"Valor inválido ({val}).\n{name.capitalize()} não pode ser maior do que {max_value}.")
			continue
		return val

def main(argv=None):
	argv = argv if argv is not None else sys.argv

	if len(argv) > 1:
		print("Este programa não aceita argumentos de linha de comando.")
		print("Use: python 3-calc_imc.py  (execute sem args e sem pipes).")
		return 3

	if not sys.stdin.isatty():
		print("Entrada não interativa detectada.\nExecute o programa sem pipe/redirecionamento:")
		print("Uso Correto: python 3-calc_imc.py")
		return 4

	PESO_MAX = 650.0
	ALTURA_MAX = 3.12

	peso = prompt_float("peso", "Digite o peso em kg (ex: 70 ou 70,0): ", 0.0, PESO_MAX)
	if peso is None:
		return 5

	altura = prompt_float("altura", "Digite a altura em metros (ex: 1.75 ou 1,75): ", 0.0, ALTURA_MAX)
	if altura is None:
		return 5

	imc = peso / (altura ** 2)
	classificacao = imcValor(imc)

	print(f"IMC: {imc:.2f}")
	print(f"Classificação: {classificacao}")
	return 0

if __name__ == "__main__":
	raise SystemExit(main())