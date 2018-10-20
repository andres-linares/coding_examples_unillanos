def check_eleven(number):
	while number > 99:
		number_as_str = str(number)
		last_digit = int(number_as_str[-1])
		truncated_number = int(number_as_str[:-1])
		number = truncated_number - last_digit
		print(number)
	if number % 11 == 0:
		print('Es divisible')
	else:
		print('No es divisible')
	print('')



while True:
	number = int(input())
	if number == 0:
		break
	check_eleven(number)