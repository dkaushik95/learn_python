furniture = ['Sofa Set', 'Dining Table',
'T.V Stand', 'Cupboard']
cost = [20000, 8500, 5499, 13920]
quantity = [0] * 4
bill = 0
for x in range(0, len(furniture)):
	quantemp = input('Enter the number of %s [Invalid is considered as 0] : '%furniture[x])
	if quantemp <= 0:
		continue
	else:
		 quantity[x] = quantemp

for x in range(0, len(furniture)):
	 bill += cost[x] * quantity[x]

print furniture
print cost
print quantity
print 'The total is %d'%bill
