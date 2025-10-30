import sys

def main():
	tokens = []
	input_source = None
	if len(sys.argv) > 1:
		fn = sys.argv[1]
		if fn != '-':
			encodings = ['utf-8', 'utf-8-sig', 'utf-16', 'latin-1', 'cp1252']
			read_success = False
			for enc in encodings:
				try:
					with open(fn, 'r', encoding=enc) as f:
						data = f.read()
						tokens = data.strip().split()
						read_success = True
						input_source = 'file'
						break
				except UnicodeDecodeError:
					continue
				except Exception as e:
					print(f"Erro ao abrir arquivo '{fn}': {e}")
					return
			if not read_success:
				print(f"Erro ao abrir/decodificar arquivo '{fn}': codificação não suportada")
				return

	if not tokens and sys.stdin.isatty():
		prog = sys.argv[0] if len(sys.argv) > 0 else '5-int-calc.py'
		msg = (
			"\nComo usar:\n forneça quatro inteiros via stdin. Exemplo:\n"
			f"  echo \"1 2 3 4\" | python {prog}\n"
			"ou se tiver um arquivo\n"
			f"  python {prog} input.txt  #(PowerShell)\n\n"
			"O programa lê 4 inteiros (em uma linha ou várias) e imprime:\n"
			"DIFERENCA = (A * B - C * D)\n"
		)
		print(msg)
		return

	if not tokens:
		tokens = sys.stdin.read().strip().split()
		input_source = 'stdin'

	if input_source == 'stdin' and len(tokens) < 4:
		try:
			while len(tokens) < 4:
				line = input()
				if not line:
					continue
				tokens.extend(line.strip().split())
		except EOFError:
			pass

	if input_source is None:
		input_source = 'stdin'

	if len(tokens) != 4:
		if input_source == 'file' and len(sys.argv) > 1:
			fn = sys.argv[1]
			print(f"Erro: arquivo '{fn}' contém {len(tokens)} valores (esperado 4).")
		else:
			print(f"Erro: foram fornecidos {len(tokens)} valores (esperado 4).")
		return

	ints = []
	for t in tokens[:4]:
		try:
			ints.append(int(t))
		except ValueError:
			print(f"Erro: valor inválido para numero inteiro: '{t}'")
			return

	a, b, c, d = ints
	diferenca = (a * b) - (c * d)
	print(f"DIFERENCA = {diferenca}")


if __name__ == '__main__':
	main()