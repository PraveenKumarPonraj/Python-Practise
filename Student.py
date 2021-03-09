def findLarge(num1,num2):
    if num1<num2:
        return 1
    elif num1>num2:
        return 2
print("enter two numbers:", end="")
num1=int(input())
num2=int(input())

res=findLarge(num1,num2)
if res==1:
    print("the greatest number is",num2)
elif res==2:    
    print("the greatest number is ",num1)
else:
    print("both are same")

