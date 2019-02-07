while True:
	try:
		a,b,=input("").split()
		a=int(a)
		b=int(b)
		break
	except:
		print("invalid input")
		break
c=1
for x in range(b):
	c=c*a
print(c)
