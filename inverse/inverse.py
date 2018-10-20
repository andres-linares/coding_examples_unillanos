def reverse_number(number):
	str_number = str(number)
	print(str_number[::-1])

while True:
	number = int(input())
	if number == 0:
		break
	reverse_number(number)