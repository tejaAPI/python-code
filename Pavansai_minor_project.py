import math
import matplotlib.pyplot as plt
#plotting the graph by taking two lists as a parameters
def graph(x1,y1):
	plt.plot(x1,y1)
	plt.show()

def bmi(mesur):
	for i in mesur:
		i['BMI']=(i['Weight']*703)/i['Height']**2
	
#finding the BMI by taking some physical attributes and applying the formula	
def combination_of_physical_attributes(mesur):
	for i in mesur:
		i["combination_of_physical_attributes"]=1.34*i["Chest_diameter"]+1.54*i["Chest_depth"]+1.20*i["Bitrochanteric"]+1.11*i["Wrist_minimum_girth"]+1.15*i["Ankle_minimum_girth"]+0.177*i["Height"]-110
		
def square(num):
	return num*num

#finding the correlation between two attributes		
def corelation(mesur,string1,string2):
	x=[]
	y=[]
	for i in mesur:
			x.append(i[string1])
			y.append(i[string2])
	xy=[]
	xsquare=[]
	ysquare=[]
	for i in range(len(x)):
		xy.append(x[i]*y[i])
		xsquare.append(square(x[i]))
		ysquare.append(square(y[i]))
	sumx=sum(x)#finding the sum for X attribute
	sumy=sum(y)#finding the sum for Y attribute
	sumxy=sum(xy)#finding the sum for XY
	sumxsquared=sum(xsquare)#finding the sum of X^2 
	sumysquared=sum(ysquare)#finding the sum of Y^2
	n=len(x)
	slope=((n*sumxy)-(sumx*sumy))/(n*sumxsquared-sumx*2)#slope formula
	intercept=(sumy-(slope*sumx))/n#intercept formula
	#finding the correlation coefficient
	correlation_coefficient=(n*sumxy-(sumx*sumy))/math.sqrt((n*sumxsquared-sumx**2)*(n*sumysquared-sumy**2))
	return(slope,intercept,correlation_coefficient,x,y)
#finding a regression line by passing one attribute,slope and intercept as a parameter
def reg_line(slope,intercept,x):
	y=[]
	print(slope,intercept)
	for i in x:
		a=intercept+slope*i
		y.append(a)
	return(y)
#reading the body measurements from a file
f=open("body.txt",'r')
record={}
#storing the each person record in a dictionary
measurements=[]	
for l in f:
	l=l.strip()
	l=l.split()
	record={}
	record["Biacromial"]=float(l[0])
	record["Biiliac"]=float(l[1])
	record["Bitrochanteric"]=float(l[2])
	record["Chest_depth"]=float(l[3])
	record["Chest_diameter"]=float(l[4])
	record["Elbow_diameter"]=float(l[5])
	record["Wrist_diameter"]=float(l[6])
	record["Knee_diameter"]=float(l[7])
	record["Ankle_diameter"]=float(l[8])
	record["Shoulder_girth"]=float(l[9])
	record["Chest_girth"]=float(l[10])
	record["Waist_girth"]=float(l[11])
	record["Navel_girth"]=float(l[12])
	record["Hip_girth"]=float(l[13])
	record["Thigh_girth"]=float(l[14])
	record["Bicep_girth"]=float(l[15])
	record["Forearm_girth"]=float(l[16])
	record["Knee_girth"]=float(l[17])
	record["Calf_maximum_girth"]=float(l[18])
	record["Ankle_minimum_girth"]=float(l[19])
	record["Wrist_minimum_girth"]=float(l[20])
	record["Age"]=float(l[21])
	record["Weight"]=float(l[22])/100
	record["Height"]=float(l[23])
	record["Gender"]=float(l[24])
	measurements.append(record)


bmi(measurements)
combination_of_physical_attributes(measurements)
corelation_bmi_age=list(corelation(measurements,'BMI','Age'))
corelation_weight_physical_attributes=list(corelation(measurements,'Weight','combination_of_physical_attributes'))
slope_bmi_age=corelation_bmi_age[0]
intercept_bmi_age=corelation_bmi_age[1]
x1=corelation_bmi_age[3]
y1=corelation_bmi_age[4]
slope_weight_physical_attributes=corelation_weight_physical_attributes[0]
intercept_weight_physical_attributes=corelation_weight_physical_attributes[1]
x2=corelation_weight_physical_attributes[3]
y2=corelation_weight_physical_attributes[4]

reg_bmi_age_y=reg_line(slope_bmi_age,intercept_bmi_age,x1)

#graph(x1,y1)
graph(x1,reg_bmi_age_y)




