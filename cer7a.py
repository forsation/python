letsopen = open('hellomf.txt')
for kl in letsopen : 
	print(kl)

cnt = 0
for line in letsopen : 
	cnt = cnt + 1
print('Lines in this file are :', cnt)	