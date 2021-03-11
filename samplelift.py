import logging

def lift_func():
    log_list = []
    while True:
        user_input=input("Enter the floor :")
        if(user_input.isdigit()):
            if(int(user_input)==0):
                print("you are in groung floor")
                log_list.append(int(user_input))
            elif(int(user_input)==1):
                print("you are in first floor")
                log_list.append(int(user_input))
            elif(int(user_input)==2):
                print("you are in second floor")
                log_list.append(int(user_input))
            elif(int(user_input)==3):
                print("you are in Third floor")
                log_list.append(int(user_input))
            elif(int(user_input)==4):
                print("you are in fourth floor")
                log_list.append(int(user_input))

            elif(int(user_input==5)):
                print(" Exit ")
                break
            else:
                print("incorrect try again")

    return log_list 

print(lift_func())               
                    
                    
                    
                    
                    