def formato_brl(value: float) -> str:
	return f"R$ {value:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')


def preco_total(nome: str, preco_unitario: float, quantidade: int) -> float:
	return preco_unitario * quantidade

def main() -> None:
	produto = "Cadeira Infantil"
	preco_unitario = 12.40
	quantidade = 3

	total = preco_total(produto, preco_unitario, quantidade)

	print("Detalhes da compra:")
	print(f"Nome do produto: {produto}")
	print(f"Preço unitário: {formato_brl(preco_unitario)}")
	print(f"Quantidade: {quantidade}")
	print(f"Preço total: {formato_brl(total)}")

if __name__ == "__main__":
	main()