'''a=int(input("Enter the first number:"))
b=int(input("Enter the first number:"))
n=0
for x in range(1,min(a,b)+1):
    if a%x==b%x==0:
        n=n+1
print(n)'''

'''def div(x,y):
    i=1
    while(i<=x and i<=y):
        if(x%i==0 and y%i==0):
            z=i
        i+=1
    return z
'''

A=[]
a=int(input("Enter any no:"))
b=int(input("Enter any no:"))
i=1
while(i<=a or i<=b ):
    if(a%i==0 or b%i==0):
        A.append(i)
    i+=1
print(A)
        
