print "Lacos"
a = 1
x = input("1-Para contar de 1 a 10\n2-Para contar de 10 a 1\n")
if x == 1:
  while True:
		print a
		a = a + 1
		if a == 11:
			break
elif x == 2:
	a = 10
	while True:
		print a
		a = a -1
		if a == -1:
			break
