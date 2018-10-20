def evaluate_surround(matrix, i, j):
	partial_sum = 0
	for m in range(-1, 2):
		for n in range(-1, 2):
			if i - m < 0 or j - n < 0:
				continue
			try:
				partial_sum += int(matrix[i - m][j - n])
			except Exception:
				pass
			
	return partial_sum / 5 > 10

def evaluate_matrix(matrix, rows, columns):
	print(' ', end=' ')
	for i in range(int(columns)):
		print(i + 1, end=' ')

	print()
	for i in range(int(rows)):
		for j in range(int(columns)):
			if j == 0:
				print(i + 1, end=' ')

			if evaluate_surround(matrix, i, j):
				print('*', end=' ')
			else:
				print(' ', end=' ')

			if j == int(columns) - 1:
				print(i + 1, end=' ')
		print()

	print(' ', end=' ')
	for i in range(int(columns)):
		print(i + 1, end=' ')


rows, columns = input().split(' ')
matrix = []

for i in range(int(rows)):
	stars_line = input().split(' ')
	matrix.append(stars_line)

evaluate_matrix(matrix, rows, columns)