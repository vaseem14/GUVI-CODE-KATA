while True:
	try:
		a=input("")
		val=int(a)
		break
	except: 
		print("entered value is not a number")
		break
if(val>0):
	print("positive")
elif(val==0):
	print("the number is ZERO")
else:
	print("negative")
	
