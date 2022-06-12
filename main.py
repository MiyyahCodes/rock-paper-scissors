#import random module
import random 

#rules of the game
print("Rules: if the two players choose the same character, it is a tie and the game repeats:" ,  "Rock beats Scissors" ,  "Paper beats Rock" ,  "Scissors beats Paper")

def interpret(c):
    if c == "R":
        return "Rock"
    elif c == "P":
        return "Paper"
    elif c == "S":
        return "Scissors"
    
    
possible_choices = ["R", "P", "S"]

def play():  
    print("Hint:R for Rock, P for Paper, S for Scissors")
    print(" ")
    print("Player's turn..")
    user_option= input("Enter the option choosen by you:")
    while user_option not in possible_choices:
        print("An error occurred")
        user_option = input("Enter valid option:")

    print("CPU'S Turn..")    
    computer_option = random.choice(possible_choices)
    print(f"\n player({interpret(user_option)}) : CPU({interpret(computer_option)}).\n")
    
    if user_option == computer_option:
        print("No winner.it is a tie!")
        print("we are starting again!")
        print("")
        play()

    if user_option == "R" and computer_option == "S":
        print("Rock beats Scissors!")
        print("You are the winner!")
    elif user_option == "S" and  computer_option =="R":
        print("Rock beats Scissors!")
        print("You loose!, CPU wins!.")
    if user_option == "S" and computer_option == "P":
        print("Scissors beats Paper!")
        print("You are the winner!")
    elif user_option == "P" and  computer_option =="S":
        print("Scissors beats Paper!")
        print("You loose!, CPU wins!.")
    if user_option == "P" and computer_option == "R":
        print("Paper beats Rock!")
        print("You are the winner!")
    elif user_option == "R" and  computer_option =="P":
        print("Paper beats Rock!")
        print("You loose!, CPU wins!.")
play()
    
    
    



         


        
    


