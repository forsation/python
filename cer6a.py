# site which i use !!! given below is G-mail
bmc="samvidghosh@gmail.com"

print(bmc[3:13])

if 'k' in bmc :
	print("got that right")
#thats called learning !!!

print(bmc.lower())	
# its actually try. i tried to type it but remembered that it's a keyword.
ty = bmc.replace('m', 'ass')
print(ty)

kn = bmc.lstrip()
df = bmc.rstrip()
ds = bmc.strip()
# trying something new !!!
bmc.startswith('p')
print(bmc)
# this thing down there is cool !!!
fmc = bmc.find('@')
print(fmc)
gmc = bmc.find('.com',fmc)
print(gmc)

found_it = bmc[fmc + 1 : gmc + 4]
print(found_it)
