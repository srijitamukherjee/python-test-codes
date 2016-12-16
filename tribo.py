a = 0
b = 1
c = 2
print a
print b
print c
for x in range ( 1, 10 ) :
	
	d=a+b+c
	a=b
	b=c
	c=d
	print d
	
