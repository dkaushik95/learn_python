bill_id = 1001
customer_id = 101
bill_amount = 500
total = 0
discount = 0

if bill_amount >= 1000:
	total = bill_amount - bill_amount * 5/100
elif bill_amount >= 500 and bill_amount < 1000:
	total = bill_amount - bill_amount*2/100
else:
	total = bill_amount - bill_amount*1/100

print ( 'Final Bill = Rs. %d' %total )
