openitbro = input('Enter the full name of the file : ')
try : 
	openit = open(openitbro)
except : 
	print('Enter the file name correctly : ', openitbro, 'does not exist')
	quit()
cnt = 0
for lines in openit : 
	if lines.startswith('From') : 
		cnt = cnt + 1
		print('Number of lines which start From : ', cnt, 'in', openit)	