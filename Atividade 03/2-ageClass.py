import sys

def classificacao(age: int) -> str:
	if age <= 12:
		return "Criança"
	if 13 <= age <= 17:
		return "Adolescente"
	if 18 <= age <= 59:
		return "Adulto"
	return "Idoso"

def idadeUsuario() -> int:
	while True:
		entrada = input("Digite sua idade: ").strip()
		if entrada == "":
			print("Entrada vazia — por favor digite um número inteiro.")
			continue
		try:
			idade = int(entrada)
		except ValueError:
			print("Valor inválido — digite um número inteiro sem decimais.")
			continue
		if idade < 0:
			print("Idade não pode ser negativa. Tente novamente.")
			continue
		return idade

def main() -> None:
	if not sys.stdin.isatty():
		print(
			"Entrada via pipe/redirecionamento detectada.\n Por favor execute: python 2-ageClass.py e digite a idade quando for solicitado."
		)
		sys.exit(1)

	if len(sys.argv) > 1:
		print(
			"Por favor execute apenas:\n python 2-ageClass.py\n —> argumentos de linha de comando não são permitidos."
		)
		sys.exit(1)

	idade = idadeUsuario()
	categoria = classificacao(idade)
	print(f"Classificação: {categoria}")

if __name__ == "__main__":
	main()