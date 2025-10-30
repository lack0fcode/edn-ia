def fomato_moeda(value: float) -> str:
	return f"R$ {value:.2f}"

def main() -> None:
	nome_produto = "Camiseta"
	preco_original = 50.00
	percentual_desconto = 20

	valor_desconto = preco_original * percentual_desconto / 100
	preco_final = preco_original - valor_desconto

	print("Detalhes do desconto:")
	print(f"Nome do produto: {nome_produto}")
	print(f"Preço original: {fomato_moeda(preco_original)}")
	print(f"Porcentagem de desconto: {percentual_desconto}%")
	print(f"Valor do desconto: {fomato_moeda(valor_desconto)}")
	print(f"Preço final: {fomato_moeda(preco_final)}")

if __name__ == "__main__":
	main()