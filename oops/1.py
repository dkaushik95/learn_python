class Customer:
	def __init__(self, cid = 1000):
		self.__customerid = cid+1
	def setcustomerid(self, cid):
		self.__customerid = cid
	def getcustomerid(self):
		return self.__customerid
	def totalcustomers(self):
		return 0
objcust = Customer()
print "Customer ID ",objcust.getcustomerid()
objcust2 = Customer()
print "Customer ID ",objcust2.getcustomerid()