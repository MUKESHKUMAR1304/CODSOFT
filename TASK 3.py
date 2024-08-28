import random
import string

def generatePassword(length):
    characters = string.ascii_letters + string.punctuation + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Enter a positive number.")
            else:
                break
        except ValueError:
            print("Wrong input. Enter a valid number to generate the password.")
    
    password = generatePassword(length)
    print("GENERATED PASSWORD:", password)

if __name__ == "__main__":
    main()
