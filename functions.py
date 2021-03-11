log_list=[]
start=0
end=5
def input_user():  
    
    user_input=int(input("Enter the floor from 1 to 4:"))
    
    return user_input

    
def my_function(user_input,start=0):
    if(start < user_input):
        print(" You are in ", user_input, "floor")
        log_list.append(user_input)
        user_input_two = int(input("Enter the floor you want to go:"))
        log_list.append(user_input_two)
        if(user_input_two != user_input):
            user_input = user_input_two
           

        else:
            print("Entered value is same:")

    
    print(" Log list:", log_list)
    if(user_input >= 5):
        print("incorrect, please try again")
    else:
        return True    
    

if __name__ == "__main__":
    num = input_user()
    check_func = my_function(num)
 
    
   
    