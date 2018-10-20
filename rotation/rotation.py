def transform(word):
	translations = len(word)
	for i in range(translations):
		print(word[i:], end='')
		print(word[:i])

words = int(input())
for i in range(words):
	word = input()
	transform(word)
	print('')