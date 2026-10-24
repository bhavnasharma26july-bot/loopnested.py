# Write a Python program for 3 students.

# For each student, ask them to enter marks for 2 subjects.

n=1
sum=0
while n<=3:
    name=input('enter your name')
    print('hi',name,'you have to enter marks of your 5 subjects') 
    for i in range(1,6):
        marks=int(input('enter your marks'))
        sum+=marks
    print('average=',sum/5,name,sum)     
    n=n+1
    sum=0
    
    