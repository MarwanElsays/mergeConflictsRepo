import random
# Random Number Generator Program
# It is made up of two functions: main_menu() and generate_random_number(),
# and a while loop that runs the program.
def main_menu():
    # Main menu has been modified to be more user friendly
    print('''Welcome to the Random Number Generator!/n
             Main Menu:                             /n
             1. Generate a random number            /n
             2. Exit                                /n
             ''')
    choice = input("Enter your choice: ")
    return choice

def generate_random_number():
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))
    print(f"Random number between {lower} and {upper}: {random.randint(lower, upper)}")
    
while True:
    pass