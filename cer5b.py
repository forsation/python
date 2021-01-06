larg_so = 0
print('before', larg_so)

for tr_num in [2,34,56,34,56,3,23,4556,33] :

	if tr_num > larg_so :
	   larg_so = tr_num
	   print(larg_so, tr_num)

print('after', larg_so)
