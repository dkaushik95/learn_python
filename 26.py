# string1 = raw_input('Enter a string')
string3 = 'khvkasasfhluvhashflaiwuhc'
string3 = string3.lower()
small = 'abcdefghijklmnopqrstuvwxyz'
diction={}
for x in list(small):
	diction[x]=0
for x in diction:
	diction[x]=string3.count(x)
print {x for x in diction if diction[x]!=0}
print diction