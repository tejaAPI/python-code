def check(ref_file,word):
	file=open(ref_file,'r')
	print("The word which is spelt wrong:",word)
	l=[]
	print("The word suggestions are...")
	word=word[:4]
	file.seek(0,0)
	for line in file:
		line=line.strip()
		if line.startswith(word):
			l.append(line)
	file.seek(0,0)
	file.close()
	return l
ref_file=input("enter reference file name:") 
data_file=input("Type your filename for spell checking: ")
#word = word.lower()
r_file= open(ref_file, "r")
d_file=open(data_file,'r')
d_list=d_file.read().split()
r_list=r_file.read().split()
print(d_list)
#print(r_list)
f=0
#if 'creative' in r_list:
	#print("teja")

for x in d_list:
	if x.lower() in r_list:
		success=True
	else:
		success=False
	if success==False:
		l=check(ref_file,x.lower())
		print(l)
		d={}
		for x in range(len(l)):
			d[x]=l[x]
		print(d)
		print("select one word from the suggestions above and give your input:")
		word=d[int(input("enter a number by seeing the keys of dictionary:"))]
		
		

	
    

    

