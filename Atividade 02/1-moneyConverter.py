def converter(reais: float, taxa: float) -> float:
	if taxa == 0:
		raise ValueError("A taxa de conversão não pode ser zero.")
	return reais / taxa

def main():
	valor_reais = 100.00
	taxa_dolar = 5.60
	taxa_euro = 6.60

	valor_dolar = converter(valor_reais, taxa_dolar)
	valor_euro = converter(valor_reais, taxa_euro)

	print(f"Valor em reais: R$ {valor_reais:.2f}")
	print(f"Taxa do dólar: R$ {taxa_dolar:.2f}  -> Valor em Dólares: US$ {valor_dolar:.2f}")
	print(f"Taxa do euro: R$ {taxa_euro:.2f}    -> Valor em Euros: € {valor_euro:.2f}")

if __name__ == "__main__":
	main()