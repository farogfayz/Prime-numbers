num = int(input("please give a number ->"))
count=0
number=[]
if num>1:
    for i in range(2,num):
        if num%i==0:
            number.append(i)
            count +=1
        else:
            count +=1
            
    if len(number)>0:
        print(num,"is a composite number and the factors are ->",number)
        print("with first method number of iterations is :", count)
    else:
        print(num,"is a prime number")
        print("with first method number of iterations is :", count)
i=2
b=math.sqrt(num)

while num>1 and i<=b:
    while num/i :
        num = num/i
        b=math.sqrt(num)
    i =i+1
print("with 2nd method number of iteration is: ",i)
