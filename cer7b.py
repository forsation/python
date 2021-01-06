openitbro = open('hellomf.txt')

for lines in openitbro : 
	lines = lines.rstrip()
	if lines.startswith('From :') : 
	print(lines)
	elif not 'that' in lines : 
		continue
	print(lines)	
		

