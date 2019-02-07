while True:
	try:
		a=input("")
		val=int(a)
		break
	except: 
		print("Invalid")
		break
if(val%2):
	print("Even")

else:
	print("Odd")
	
