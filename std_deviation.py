import csv 
import math
with open("data.csv", newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
data=file_data[0]

#step1: Finding the mean
def mean(data):
    n=len(data)
    total=0
    for i in data:
        total+=int(i)
    mean=total/n
    return mean

#step2: Squaring and getting the value
squared_list=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squared_list.append(a)

#step3: Getting the sum of square list
sum=0
for i in squared_list:
    sum=sum+i

#step4: Dividing the sum by the total value
result=sum/(len(data)-1)

#step5: Getting the standard deviation by taking square root
std_deviation=math.sqrt(result)
print("The Standard Deviation Is:=>", std_deviation)
