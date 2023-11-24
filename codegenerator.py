import random
import string

def generate_password(length):
   
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

   
    length = max(length, 8)

   
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
   
    password_length = int(input("Enter the desired length of the password: "))

   
    generated_password = generate_password(password_length)

    print("Generated Password: ", generated_password)

if __name__ == "__main__":
    main()
