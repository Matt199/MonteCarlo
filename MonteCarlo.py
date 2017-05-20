import random
import math 



# Definition of the calculatwed function 

def function(x): 
	
	return (pow(x,2) + 2 * x + 4)

# Randomize points of the integration interval 

	
def randomizePoints(min, max): 

	return random.uniform(min,max)
	
# main funtion 


integral = 0.0
average = 0.0
print("Enter the integration interval")
print("")
first = raw_input("Enter the begining of the integration interval: ")
last = raw_input("Enter the end of the integration interval: ")
	
first = float(first)
last = float(last)
	
# accuracy level 	
	
accuratcyLevel = raw_input("Enter the accuracy level of the integration: ")

accuratcyLevel = int(accuratcyLevel)

accuratcyLevel *= 100

for i in range(0, accuratcyLevel+1):
	integral += function(randomizePoints(first,last))
	#print(integral)


# calculate integral 

average = (integral / float(accuratcyLevel))
integral = (last - first) * average

print(integral)
	
	
	
	
	
	
	
	

	
	

