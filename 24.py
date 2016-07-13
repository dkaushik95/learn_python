string1 = raw_input('Enter A String : ')
punctuations = '!()-[]{},<>./?@#$%^&*_~'
string1= ''.join( c for c in string1 if  c not in punctuations )
print(string1)
