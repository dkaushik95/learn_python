def check_baggage(baggage_amount):
	if baggage_amount > 0 and baggage_amount <= 40:
		return True
	else:
		return False
def check_immigration(expiry_year):
	if expiry_year >= 2001 and expiry_year <= 2025:
		return True
	else:
		return False
def check_security(noc_status):
	return noc_status
def traveler():
	traveler={
		'traveler_id': 1001,
		'traveler_name': 'Jim',
		'baggage_amount': 35,
		'expiry_year': 2019,
		'noc_status': True
	}
	if check_baggage(traveler['baggage_amount']) and check_immigration(traveler['expiry_year']) and check_security(traveler['noc_status']):
		print traveler['traveler_name'], traveler['traveler_id']
		print 'Allow traveller to fly!'
	else:
		print traveler['traveler_name'], traveler['traveler_id']
		print 'Detail traveller for Re-checking!'
traveler()