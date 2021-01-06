x = [23,45,34,34]
y = [546,456,46,56,45,645,6]
z = x + y
print(z)
a = y[0:5]
print(a)

h = type(a)
print(h)

f= dir(h)
print(f)

stuff = list()
stuff.append('hutu')
stuff.append(34545)
print(stuff) 
g = 'hutu' in stuff
print(g)

sd = y.sort()
print(sd)
print('average of numbers : ', sum(y)/len(y))
