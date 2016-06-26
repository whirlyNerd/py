def maximum(x,y):
	if x > y:
		return x
	elif x == y:
		return 'The numbers are equal'
	else: 
		return y
		
x = int(raw_input('Enter an integer for x: ')) 
y = int(raw_input('Enter an integer for y: '))
		
print maximum(x,y)