import random
import string

# Function to generate a random password
def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

# Main logic to handle user interactions
def password_generator():
    length = int(input("Enter the desired password length: "))

    while True:
        password = generate_password(length)
        print("Your generated password is:", password)

        # Ask the user if they like the password
        user_choice = input("Do you like this password? (yes or no): ").lower()

        if user_choice == 'yes':
            print("Great! Enjoy your secure password!")
            break  # Exit loop if the user is satisfied
        elif user_choice == 'no':
            print("Generating a new password...")
        else:
            print("Invalid choice. Please respond with 'yes' or 'no'.")

# Run the password generator
password_generator()

