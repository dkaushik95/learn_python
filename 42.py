def reverse_a_string(given_string):
	if len(given_string) <= 1:
		return given_string
	return reverse_a_string(given_string[1:]) + given_string[0]
print reverse_a_string('Hello')
print reverse_a_string('mississipi')