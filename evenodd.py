while True:
	try:
		a=input("")
		val=int(a)
		break
	except: 
		print("invalid input ")
		break
if(val%2==0):
	print("Even")

else:
	print("Odd")
	
