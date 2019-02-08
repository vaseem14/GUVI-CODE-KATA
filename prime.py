a=int(input())
p=0
for x in range(2,a//2+1):
	if(a%x==0):
		p=p+1
if(p<=0):
	print("yes")
else:
	print("no")
