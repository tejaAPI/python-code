#simple rule based classifier
#predicting the employee class i.e., wether a person is getting >50k or <50k bucks annually
#reading the employee data fron the files 
def makeTrainingSet(filename):
    print("Reading in training data...")
    f=open(filename,'r')#Reading the employee data from the file
    #creating a list of dictionaries to store the data of each employee
	trainingset=[] 
    for l in f:
    
        l=l.strip()
        line_list=l.split(',')
        #creating a dictionary for evrey employee record
		record={}
        record['age']=float(line_list[0])
        record['workclass']=line_list[1]
        record['educationnum']=float(line_list[4])
        record['marital']=line_list[5]
        record['occupation']=line_list[6]
        record['relationship']=line_list[7]
        record['race']=line_list[8]
        record['sex']=line_list[9]
        record['capitalgain']=float(line_list[10])
        record['capitalloss']=float(line_list[11])
        record['hours']=float(line_list[12])
        record['class']=line_list[14]
        trainingset.append(record)
    f.close()
    print("Done reading training data...")
    return trainingset
#creating a classifier by finding the averages for continous attributes and ratios for non-continuos attributes    
def trainclassifier(c):
    print('Training classifier...')
	#Taking two dictionaries one for >50k and one for <50k
    d1={}
    d2={}
    avg1=0
    avg2=0
    age1=0
    age2=0
    count1=0
    count2=0
    educationnum1=0
    educationnum2=0
    capitalgain1=0
    capitalgain2=0
    capitalloss1=0
    capitalloss2=0
    hours1=0
    hours2=0
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    l5=[]
    l6=[]
    l7=[]
    l8=[]
    l9=[]
    l10=[]
    l11=[]
    l12=[]
    for x in c:
        if x['class']=="<=50K":
            age1+=x['age']
            count1+=1
            educationnum1+=x['educationnum']
            capitalgain1+=x['capitalgain']
            capitalloss1+=x['capitalloss']
            hours1+=x['hours']
            l1.append(x['workclass'])
            l2.append(x['marital'])
            l3.append(x['occupation'])
            l4.append(x['relationship'])
            l5.append(x['race'])
            l6.append(x['sex'])
        else:
            age2+=x['age']
            count2+=1
            educationnum2+=x['educationnum']
            capitalgain2+=x['capitalgain']
            capitalloss2+=x['capitalloss']
            hours2+=x['hours']
            l7.append(x['workclass'])
            l8.append(x['marital'])
            l9.append(x['occupation'])
            l10.append(x['relationship'])
            l11.append(x['race'])
            l12.append(x['sex'])
	#finding the averages for continuos attributes
	#Appending the each attribute average into a dictionary
    avg1=age1//count1
    avg2=age2//count2
    d1['age']=avg1
    d2['age']=avg2
    avg1=educationnum1//count1
    avg2=educationnum2//count2
    d1['educationnum']=avg1
    d2['educationnum']=avg2
    avg1=capitalgain1//count1
    avg2=capitalgain2//count2
    d1['capitalgain']=avg1
    d2['capitalgain']=avg2
    avg1=capitalloss1//count1
    avg2=capitalloss2//count2
    d1['capitalloss']=avg1
    d2['capitalloss']=avg2
    avg1=hours1//count1
    avg2=hours2//count2
    d1['hours']=avg1
    d2['hours']=avg2
    d1['workclass']={}
    d2['workclass']={}
    d1['marital']={}
    d2['marital']={}
    d1['occupation']={}
    d2['occupation']={}
    d1['relationship']={}
    d2['relationship']={}
    d1['race']={}
    d2['race']={}
    d1['sex']={}
    d2['sex']={}
    d1['class']='<=50K'
    d2['class']='>50K'
    count1=0
	#finding the ratios for non-continous attributes and appending into the dictionary
    for index in range(0,len(l1)):
            if l1[index] not in list(d1['workclass'].keys()):
                count1+=l1.count(l1[index]) 
                d1['workclass'][l1[index]]=count1/len(l1)
   
    for index in range(0,len(l7)):
            if l7[index] not in list(d2['workclass'].keys()):
                count1+=l7.count(l7[index]) 
                d2['workclass'][l7[index]]=count1/len(l7)
    for index in range(0,len(l2)):
            if l2[index] not in list(d1['marital'].keys()):
                count1+=l2.count(l2[index]) 
                d1['marital'][l2[index]]=count1/len(l2)
    for index in range(0,len(l8)):
            if l8[index] not in list(d2['marital'].keys()):
                count1+=l8.count(l8[index]) 
                d2['marital'][l8[index]]=count1/len(l8)
    for index in range(0,len(l3)):
            if l3[index] not in list(d1['occupation'].keys()):
                count1+=l3.count(l3[index]) 
                d1['occupation'][l3[index]]=count1/len(l3)
    for index in range(0,len(l9)):
            if l9[index] not in list(d2['occupation'].keys()):
                count1+=l9.count(l9[index]) 
                d2['occupation'][l9[index]]=count1/len(l9)
    for index in range(0,len(l4)):
            if l4[index] not in list(d1['relationship'].keys()):
                count1+=l4.count(l4[index]) 
                d1['relationship'][l4[index]]=count1/len(l4)
        
    for index in range(0,len(l10)):
            if l10[index] not in list(d2['relationship'].keys()):
                count1+=l10.count(l10[index]) 
                d2['relationship'][l10[index]]=count1/len(l10)
    for index in range(0,len(l5)):
            if l5[index] not in list(d1['race'].keys()):
                count1+=l5.count(l5[index]) 
                d1['race'][l5[index]]=count1/len(l5)
    for index in range(0,len(l11)):
            if l11[index] not in list(d2['race'].keys()):
                count1+=l11.count(l11[index]) 
                d2['race'][l11[index]]=count1/len(l11)
    for index in range(0,len(l6)):
            if l6[index] not in list(d1['sex'].keys()):
                count1+=l6.count(l6[index]) 
                d1['sex'][l6[index]]=count1/len(l6)
    for index in range(0,len(l12)):
            if l12[index] not in list(d2['sex'].keys()):
                count1+=l12.count(l12[index]) 
                d2['sex'][l12[index]]=count1/len(l12)
    
        
              
    print("Done training classifier...")
    return (d1,d2)
#creating the test set to classify the employess     
def makeTestSet(filename):
    print("Reading in test data...")

    testset=makeTrainingSet(filename)
    for record in testset:
    
       record['predicted']='unknown'
    print("Done reading test data...")

    return testset
#classifying the employee by comparing the employee data and classifier data
def classifyTestRecords(testset,d1,d2):
    print("Classifying the records...")
    for record in testset:
        v1=0#votes for <=50k
        v2=0#votes for >50k
		#classifying the data on continuos attributes
        
        """
        if (record['age']<=d1['age']):
            v1+=1
        else:
            v2+=1
        if(record['educationnum']<=d1['educationnum']):
            v1+=1
        else:
            v2+=1
        if(record['capitalgain']<=d1['capitalgain']):
            v1+=1
        else:
            v2+=1
        if(record['capitalloss']<=d1['capitalloss']):
            v1+=1
        else:
            v2+=1
        if(record['hours']<=d1['hours']):
            v1+=1
        else:
            v2+=1
        """
		#classifying the data on no continuos attributes
        if d1['relationship'][record['relationship']]>=d2['relationship'][record['relationship']]:
            v1+=1
        else:
            v2+=1
        if d1['marital'][record['marital']]>=d2['marital'][record['marital']]:
            v1+=1
        else:
            v2+=1
        if d1['occupation'][record['occupation']]>=d2['occupation'][record['occupation']]:
            v1+=1
        else:
            v2+=1
        if d1['sex'][record['sex']]>=d2['sex'][record['sex']]:
            v1+=1
        else:
            v2+=1
        if record['workclass']!='Without-pay':
            if d1['workclass'][record['workclass']]>=d2['workclass'][record['workclass']]:
                v1+=1
            else:
                v2+=1
        if d1['race'][record['race']]>=d2['race'][record['race']]:
            v1+=1
        else:
            v2+=1 
                
        if v1>v2:
            record['predicted']='<=50K'
        else:
            record['predicted']='>50K'
            
        
    print("Done classifying.")   
    return testset

#reporting the accuracy i.e., how many classified records are correct
def reportAccuracy(testset):
    c=0
    for record in testset:
        if record['class']==record['predicted']:
            c+=1
    print("Correct: ",c)
    print("Total: ",len(testset))
    print("Accuracy (as a percentage): ",(c/len(testset))*100,"%")
    print("Program Finished")
#calling all the above functoins
def main():
    c=makeTrainingSet("trainingdata.txt")
    x,y=trainclassifier(c)
    a=makeTestSet("testdata.txt")
    b=classifyTestRecords(a,x,y)
    reportAccuracy(b)
    print(x)
    print(y)
    return
main()
          

    
    
            
   