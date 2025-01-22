# Random Number Generator Program
# It is made up of two functions: main_menu() and generate_random_number(),
# and a while loop that runs the program.
def main_menu():
    print("Welcome to the Random Number Generator!")
    print("1. Generate a random number")
    print("2. Exit")
    choice = input("Enter your choice: ")


def generate_random_number():
    pass
    
while True:
    choice = main_menu()
    if choice == '1':
        generate_random_number()
    elif choice == '2':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
