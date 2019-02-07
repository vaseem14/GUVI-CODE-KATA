while True:
	try:
		a,b,c=input("").split()
		a=int(a)
		b=int(b)
		c=int(c)
		break
	except: 
		print("invalid input ")
		break
if (a>b):
		if(a>c):
				print(a)
		elif c>a:
				print(c)
elif (b>a):
		if (b>c):
			print(b)
		elif c>b:
				print(c)
