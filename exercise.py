def input_user():
    log_list = []
    start = 0
    end = 5
    user_input=int(input("Enter the floor you want to go:"))
    

    if(start < user_input):
        print(" You are in ", user_input, "floor")
        log_list.append(user_input)
        user_input_two = int(input(" Enter the floor you want to go:"))
        log_list.append(user_input_two)
        if(user_input_two != user_input):
            user_input = user_input_two
           

        else:
            print("Entered value is same:")

    
    print(" Log list:", log_list)
    if(user_input >= 5):
        print(" Incorrect,please try again")
    return input_user





if __name__ == "__main__":
   
    input_user()