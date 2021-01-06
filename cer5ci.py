smallest = None
for valu in [23,45,23,45,5,6,565,5,5,56,5,54,3,4,32,3,35,6,67,7,89,8,7,5] :
	if smallest is None :
		smallest = valu
    elif valu < smallest:
        smallest = valu 
        print(smallest, valu)

print('after' , smallest)        
	
