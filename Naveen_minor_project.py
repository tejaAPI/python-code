#Analysing the states data 
from prettytable import PrettyTable
import pylab
import math
def states_data():
	f=open("statedata.txt")
	c=1
	region=input("enter region:")
	s={}
	li=[]
	for line in f:
		if c==1:
			l1=line.split(",")
			c+=1	
			break
	for line in f:
		if c>=2:
			l2=line.split(",")
			x=float(l2[3])/float(l2[2])
			y=float(l2[4])/float(l2[2])
			l2.append(x)
			l2.append(y)
			
			
			
			if region==l2[1].lower():
				l2[-1]=l2[-3][:-1]
				li.append(l2)
				l=l2[2:]
				c=0
				for x in l:
					l[c]=float(x)
					c+=1
				s[l2[0]]=l
				
				
			
	print(s,"\n")
	return (s,li)
def print_region_info(s,li):
	max1=0
	max2=0
	min1=None
	min2=None
	for state,x in s.items():
		if max1<=x[1]:
			max1=x[1]
			max_state1=state
		if max2<=x[2]:
			max2=x[2]
			max_state2=state
		if min1 is None:
			min1=x[1]
			min1_state1=state
		elif min1>=x[1]:
			min1=x[1]
			min_state1=state
		if min2 is None:
			min2=x[2]
			min_state12=state
		elif min2>=x[2]:
			min2=x[2]
			min_state2=state
		
			
	print(max_state1,"is having highest GDP(Gross Domestic Product) that is",max1,"$\n")
	print(min_state1,"is having lowest GDP(Gross Domestic Product) that is",min1,"$\n")
	print(max_state2,"is having highest PI(Personal Income) that is",max2,"$\n")
	print(min_state2,"is having lowest PI(Personal Income) that is",min2,"$\n")
	t=PrettyTable(['State','region','Population(m)','GDP(b)','Income(b)','Subsidies(m)','Compensation(b)','Taxes(b)','GDP per capita','Income per capita'] )
	for x in li:
		t.add_row(x)
	print(t)
	return t
	
def draw_graph(s,li,t):
	state=list(s.keys())
	print("0.Pop\n1.GDP\n2.PI\n3.Sub\n4.CE\n5.TPI\n6.GDPp\n7.Pip\n")
	print("For which parameters you want to draw the graphs....give the parameters with comma separated values...")
	X,Y=input().split(",")
	X=int(X)
	Y=int(Y)
	x=[]
	y=[]
	for k1 in s.values():
		x.append(k1[X])
		y.append(k1[Y])
	
	for i,txt in enumerate(state):
		pylab.annotate(txt, (x[i],y[i]))
	#print(x)
	#print(y)
	
	slope,intercept,corelation_coeff=corelation(x,y)
	y_reg=reg_line(slope,intercept,x)
	pylab.plot(x,y_reg,'-r')
	pylab.scatter(x,y)
	pylab.scatter(x,y_reg,)
	pylab.show()
	  
	return (x,y)
def square(num):
	return num*num
def corelation(x,y):
	#for i in mesur:
			#x.append(i[string1])
			#y.append(i[string2])
	xy=[]
	xsquare=[]
	ysquare=[]
	for i in range(len(x)):
		xy.append(x[i]*y[i])
		xsquare.append(square(x[i]))
		ysquare.append(square(y[i]))
	sumx=sum(x)
	sumy=sum(y)
	sumxy=sum(xy)
	sumxsquared=sum(xsquare)
	sumysquared=sum(ysquare)
	n=len(x)
	slope=((n*sumxy)-(sumx*sumy))/(n*sumxsquared-sumx**2)
	intercept=(sumy-(slope*sumx))/n
	correlation_coefficient=(n*sumxy-(sumx*sumy))/math.sqrt((n*sumxsquared-sumx**2)*(n*sumysquared-sumy**2))
	return(slope,intercept,correlation_coefficient)
def reg_line(slope,intercept,x):
	y=[]
	print(slope,intercept)
	for i in x:
		a=intercept+slope*i
		y.append(a)
	return(y)
	
def main():	
	s,li=states_data()
	t=print_region_info(s,li)
	x,y=draw_graph(s,li,t)
	
	
main()




		