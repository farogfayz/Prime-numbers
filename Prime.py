
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
