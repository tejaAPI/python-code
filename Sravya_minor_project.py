#Spelling checker and giving the word suggestions for wrongly spelt word
def check(ref_file,word):
	file=open(ref_file,'r')
	print("The word which is spelt wrong:",word)
	#intialising a list for word suggestions
	l=[]
	print("The word suggestions are...")
	word=word[:4]
	file.seek(0,0)
	#comparing the given word with every word in the file
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
ref_file= open(ref_file, "r")#Reference file
data_file=open(data_file,'r')#Testing file which contains a paragraph
data_list=d_file.read().split()#splitting the paragraph into words 
ref_list=r_file.read().split()#which contains the word
#print(data_list)
#print(ref_list)
f=0
#if 'creative' in r_list:
	#print("teja")

for x in data_list:
	if x.lower() in ref_list:#checking wether the word is in reference file or not
		success=True
	else:
		success=False
	#Giving the word suggestions by taking the first three charecters from wrongly spelt word
	if success==False:
		l=check(ref_file,x.lower())
		print(l)
		d={}
		for x in range(len(l)):
			d[x]=l[x]
		print(d)
		print("select one word from the suggestions above and give your input:")
		word=d[int(input("enter a number by seeing the keys of dictionary:"))]
		
		

	
    

    

