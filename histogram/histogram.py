def show_histogram(histogram, bars, bars_array):
	print('Histograma {}'.format(histogram + 1))
	max_intensity = max(bars_array)
	for i in range(max_intensity):
		for j in range(bars):
			if bars_array[j] >= max_intensity - i:
				print('*', end=' ')
			else:
				print(' ', end=' ')
		print('')

histograms = int(input())
for i in range(histograms):
	bars = int(input())
	bars_array = []
	for j in range(bars):
		intensity = len(input())
		bars_array.append(intensity)
	show_histogram(i, bars, bars_array)