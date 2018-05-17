#file operations 
f=open('bestsellers.txt')
#Taking the year range from the user
x,y=input("Enter range of years:").split(",")
x=int(x)
y=int(y)
#printing the book by checking the year
for line in f:
	line=line.strip()
	line=line.split('\t')
	year=int(line[3][-4:])
	if x<=year<=y:
		print(line)
#Taking the specific month and year
x,y=input("Enter specific month and year:").split(",")
x=int(x)
y=int(y)
print(x,y)
f.seek(0,0)
for line in f:
	line=line.strip()
	line=line.split('\t')
	lohitha=line[3]
	lohitha=lohitha.split('/')
	if x==int(lohitha[1]) and y==int(lohitha[2]):
		print(line)
f.seek(0,0)
#Giving the author name as a input
name=input("Enter any author name:")
for line in f:
	line=line.strip()
	line=line.split('\t')
	if line[1].lower().startswith(name):
		print(line)
f.seek(0,0)
#Giving the title as a input
name=input("Enter any title of the book:")
for line in f:
	line=line.strip()
	line=line.split('\t')
	if line[0].lower().startswith(name):
		print(line)
	
	


