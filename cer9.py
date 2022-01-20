k = (input('To print my stuff type "stuff" or to exit type "exit" : '))

stuff = dict()
stuff['laptop'] = 2
stuff['desktop'] = 1
stuff['Apple_products'] = 'Dont kid yourself i dont buy Apple products'
stuff['pendrive'] = 2
stuff['headphone'] = 2
stuff['mouse'] = 2
stuff['mouse1'] = 'wireless mouse'
stuff['mouse2'] = 'wired mouse'
stuff['money'] = 0	
print("\n")
for l in stuff :
	print(l)
print("\n")
if k == "stuff" :
	f = (input("If you want to know more about them then type it : "))

	if f == 'laptop' :
		print(stuff['laptop'])

		if f == 'desktop' :
			print(stuff['desktop'])

			if f == 'Apple products' :
				print(stuff['Apple_products'])

				if f == 'pendrive' :
					print(stuff['pendrive'])

					if f == 'headphone' :
						print(stuff['headphone'])

						if f == 'mouse' : 
							print(stuff['mouse'])
							T
							if f == 'money' :
								print(stuff['money'])

if k == "exit" :
	exit() 	
