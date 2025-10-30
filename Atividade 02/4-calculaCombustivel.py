def calcular_consumo(distancia_km: float, combustivel_l: float) -> float:
	if combustivel_l == 0:
		raise ValueError("Combustível gasto não pode ser zero.")
	return distancia_km / combustivel_l


def main() -> None:
	distancia = 300.0  
	combustivel = 25.0 

	consumo = calcular_consumo(distancia, combustivel)

	print(f"Distância percorrida: {distancia} km")
	print(f"Combustível gasto: {combustivel} litros")
	print(f"Consumo médio: {consumo:.2f} km/l")

if __name__ == "__main__":
	main()