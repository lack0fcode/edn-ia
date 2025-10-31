def bissexto(ano: int) -> bool:
	if ano % 4 != 0:
		return False
	if ano % 100 == 0:
		return ano % 400 == 0
	return True

def main() -> None:
	while True:
		entrada = input("Digite um ano (ou pressione Enter para sair): ").strip()
		if entrada == "":
			print("Saindo.")
			break
		try:
			ano = int(entrada)
		except ValueError:
			print("Digite um número inteiro para o ano.")
			continue

		if ano < 1583:
			print(
				"\nEntrada inválida: o conceito atual de ano bissexto começou em 1582.\n"
				"Por favor, digite um ano maior ou igual a 1583.\n")
			continue

		if bissexto(ano):
			print(f"{ano} é bissexto.")
		else:
			print(f"{ano} não é bissexto.")

if __name__ == "__main__":
	main()

