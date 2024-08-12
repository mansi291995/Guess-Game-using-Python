import random
def guess_game():
    lower=1
    upper=10
    
    secret_code = random.randint(lower,upper)
    print(secret_code)
    attempts=0
    while True:
        
        try:
            user_number=input("Enter number")
            print("welcome to guess game")
            user_guess=int(user_number)
            attempts+=1
            if(user_guess < lower or user_guess > upper):
                print(f"please guess number within range from{lower} to {upper}")
                continue
            elif(user_guess < secret_code):
                print("please enter upper value ry again!!")
            elif(user_guess > secret_code):
                print("please enter lower value try again!!")
            else:
                print("congratulations!!! guess number is correct")
                break
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter a valid number.")

guess_game()