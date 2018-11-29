from math import exp

def discrete_future_value(x,r,n):
	return x*(1+r)**n

def discrete_present_value(x,r,n):
	return x*(1+r)**-n
	
def continous_future_value(x,r,t):
	return x*exp(r*t)
	
def continous_present_value(x,r,t):
	return x*exp(-r*t)

if __name__ == "__main__":
	x=100
	r=0.05
	n=5
	
	print("Future Value discrete_future_value",discrete_future_value(x,r,n))
	print("Future Value discrete_present_value",discrete_present_value(x,r,n))
	print("Future Value continous_future_value",continous_future_value(x,r,n))
	print("Future Value continous_present_value",continous_present_value(x,r,n))