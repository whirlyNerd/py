print 'Please input a string to right-justify:'
input = raw_input()

spaces = 70 - len(input)

def right_justify(input, spaces):
	print ' ' * spaces, '%s' % input
	
right_justify(input, spaces)