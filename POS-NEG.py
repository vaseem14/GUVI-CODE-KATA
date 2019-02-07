while True:
	try:
		a=input("")
		val=int(a)
		break
	except: 
		print("invalid input ")
		break
if(val>0):
	print("Positive")
elif(val==0):
	print("ZERO")
else:
	print("Negative")
	
