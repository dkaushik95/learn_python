string1 = raw_input('Enter the first string : ')
string2 = raw_input('Enter the second string : ')
string3 = string1 + string2
string4 = ''
for x in range(0, len(string3)):
	if string3[x].isupper():
		string4 += string3[x]
print string4