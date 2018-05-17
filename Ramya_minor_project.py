#sorting the one lakh numbers 
#importing the random module
import random
l=[]
count=0
print("Generating the random numbers and appending into the list.......")
#Generating the random numbers
while(count!=10000):
	x=random.randint(0,10000)
	if x not in l:#checking the number repititions
		l.append(x)
		count+=1
		print(x,"is appended....")

print("Entering the numbers from the list into the file without sorting.......")	
with open("num.txt",'w') as f:
	f.write("********Before Sorting**********\n")
	f.write(str(l))
l.sort()#applying the sort method 
print("Entering the data into the file after sorting.......")
with open("numsort.txt",'w') as s:
	s.write("*********After Sorting***********\n")
	s.write(str(l))
print("Program execution completed.......") 
	
   



