import random
# Dictionary of Rules for Who defeats Whom 
rules = {
    "Dragon" :"Warrior", # Dragon Overpowers Warrior
    "Warrior":"Thief",   # Warrior Defeats Thief
    "Thief"  :"Dragon"   # Thief steals from Dragon
}
while True:
    print('''You can choose from the following choices : 
    Dragon, Warrior, Thief or exit''')
    your_choice = input("Enter your choice : ").capitalize()

    if your_choice.lower() == "exit":
        break
    
    if your_choice not in rules:
        print("Invaid choice. Please Try Again")
        continue

    choices = ["Dragon", "Warrior", "Thief"]
    computer_choice = random.choice(choices)

    print(f"Computer choice : {computer_choice}")
    print(f"Your choice : {your_choice}")

    if your_choice == computer_choice:
        print("Its a Draw!")
    elif rules[your_choice] == computer_choice:
        print("You Win!")
    else:
        print("You Lose!")    
