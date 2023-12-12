import random

options = ["Rock","Paper","Scissors"]
user_choice = input("What do you Choose? Rock, Paper,  Scissors \n")

ramdom_num = random.randint(0,2)
#rock :0 , paper:1, scissors :2
computer_choice = options[ramdom_num]
print("Computer Chose ",computer_choice + ".")
if user_choice== "Rock" and computer_choice=="Rock":
    print("It's tie!")
elif user_choice=="Paper" and computer_choice=="Paper":
    print("It's tie!")
elif user_choice=="Scissors" and computer_choice=="Scissors":
    print("It's tie!")

elif user_choice== "Rock" and computer_choice=="Scissors" :
    print ("You win! ")

elif user_choice == "Paper" and computer_choice =="Rock":
    print("You win")

elif user_choice == "Scissors" and computer_choice =="Paper":
    print("You win")

else:
    print("You lose!")
