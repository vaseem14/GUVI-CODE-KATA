a=int(input())
z=list(map(int,str(a)))
y=list(map(lambda x:x**3,z))
if(sum(y)==a):
	print("yes")
else:
	print("no")
