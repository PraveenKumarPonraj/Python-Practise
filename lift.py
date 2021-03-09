user_input=int(input("Enter the floor you want to go :"))

for lp in range(0,5):
    if(lp==user_input):
        print("you are in " ,user_input, "floor")
if(user_input >=5):
    print("incorrect number")    