def normalizacao(u: str) -> str:
	if not isinstance(u, str):
		return ''
	s = u.strip().lower()
	if s in ('c', 'celsius', '°c'):
		return 'C'
	if s in ('f', 'fahrenheit', '°f'):
		return 'F'
	if s in ('k', 'kelvin'):
		return 'K'
	return ''

def unidade(code: str) -> str:
	return {'C': 'Celsius', 'F': 'Fahrenheit', 'K': 'Kelvin'}.get(code, code)

def simbolo(code: str) -> str:
	return {'C': '°C', 'F': '°F', 'K': 'K'}.get(code, code)

def tempConverter(value: float, src: str, dst: str) -> float:
	if src == dst:
		return value

	if src == 'C':
		c = value
	elif src == 'F':
		c = (value - 32) * 5.0 / 9.0
	elif src == 'K':
		c = value - 273.15
	else:
		raise ValueError('Unidade de origem inválida')

	if dst == 'C':
		return c
	if dst == 'F':
		return c * 9.0 / 5.0 + 32
	if dst == 'K':
		return c + 273.15

	raise ValueError('Unidade de destino inválida')

def main():
	try:
		raw = input('Informe a temperatura (ex: 36.6): ').strip()
		temp = float(raw.replace(',', '.'))
	except Exception:
		print('Entrada inválida para temperatura. Use um número, ex: 36.6')
		return

	origem = input('Unidade de origem (C, F ou K): ')
	src = normalizacao(origem)
	if not src:
		print(f'Unidade de origem inválida: "{origem}"')
		return

	destino = input('Unidade de destino (C, F ou K): ')
	dst = normalizacao(destino)
	if not dst:
		print(f'Unidade de destino inválida: "{destino}"')
		return

	try:
		result = tempConverter(temp, src, dst)
	except ValueError as e:
		print('Erro:', e)
		return

	print(f'valor convertido de {unidade(src)} para {unidade(dst)}')
	print(f'{result:.2f} {simbolo(dst)}')

if __name__ == '__main__':
	import sys, os

	if len(sys.argv) > 1:
		invoked = ' '.join(['python', os.path.basename(sys.argv[0])] + sys.argv[1:])
		print(f'Você invocou: {invoked}')
		print('Não utilize argumentos pela linha de comando.\nExecute apenas: python 4-tempConverter.py')
		sys.exit(1)

	try:
		if not sys.stdin.isatty():
			print('Entrada detectada via pipe/redirect (ex.: echo 100 C F | python 4-tempConverter.py).')
			print('Por favor execute apenas: python 4-tempConverter.py e informe os valores quando solicitado pelo programa.')
			sys.exit(1)
	except Exception:
		pass

	main()
