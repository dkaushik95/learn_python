import re

# student_id = raw_input('Enter the Student ID')
student_id = '1s234'
if len((re.match(r'\d', student_id)).groups()) != 0:
	print 'Pass'
else:
	print 'Fail'