s = []
list_size = 3
def isempty(stack):
	if len(stack) == 0:
		return True
	else:
		return False
def isfull(stack):
	if len(stack) == list_size:
		return True
	else:
		return False
def push(stack, number):
	if isfull(stack):
		print 'Stack is full!'
		return
	else:
		stack.append(number)
		print '%d Pushed!'%number
		return
def pop(stack):
	if isempty(stack):
		print 'Nothing to delete'
		return
	else:
		item = stack.pop()
		print '%d popped !'%item
		return 
def display_elements(stack):
	print stack

push(s, 12)
push(s, 24)
push(s, 70)
push(s, 28)
display_elements(s)
pop(s)
pop(s)
push(s, 15)
display_elements(s)
pop(s)
pop(s)
display_elements(s)
pop(s)