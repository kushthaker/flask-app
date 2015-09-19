myvar = 'hello'

print myvar

mylist = ['string' , 23.43, [1, 2, 3, 4, 5], True ]

for i in mylist:
	print i


num = 15

if num % 5 == 0 and num % 3 != 0: 
	print 'fizz'
elif num % 3 == 0 and num % 5 != 0:
	print 'buzz'
else:
	print 'fizzbuzz'
