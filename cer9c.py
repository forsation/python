count = dict()
para = input('Enter the lines the text  : ')
words = para.split()

print('counting  .... ')
for word in words :
	count[word] = count.get(word, 0 ) + 1
print('words : ', count)	