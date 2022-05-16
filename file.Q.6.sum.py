obj=open("sum.txt","w")
num=int(input("enter the number:-"))
sum=0
for i in range(num):
    number=int(input("enter the-:"))
    sum+=number
    a=str(sum)+"\n"
    obj.write(a)
obj.close()



# a=int(input("enter the num:-"))
# sum=0
# for i in range(a):
#     b=int(input("enter the number:- "))
#     sum=sum+b
# print(sum)