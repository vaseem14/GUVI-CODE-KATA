a=input("")	
a=int(a)
if(a>1):
	for x in range(2,a):
			if(a%x==0):
				print("no")
				break
			else:
				print("yes")
				break
else:
	print("no")
