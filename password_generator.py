# INF360B - Programming in Python
# Choun Chan Nirak
# Midterm Project

"""
This is a password generator program. It will be automatically be copied to your clipboard.
You can get the generated password either running the program in an IDE
or using terminal command by typing the filename. 

To set up typing filename in the terminal command, following these instructions:
    ** Windows **
    1. Create a new file in Notepad.
    2. Place this command into it:
        @py.exe C:\path_to_file\password_generator.py %*
        @pause 
    3. Save it as password_generator in C:\Windows folder.
    4. From now on, you can just run it through the command prompt by just typing the filename (password_generator).

    ** MacOS **
    1. Create a new file in TextEdit
    2. Place this command into it:
        #!/usr/bin/env bash
        python3 /path/to/your/pythonScript.py
    3. Save it as .command file extension in your home folder (for example, on my computer it’s /Users/Nirak)
    4. Open your terminal window and run this shell script:
        chmod u+x password_generator.command (This is what I name in step 3)
    5. From now on, you can just run in through the Spotlight icon (or press image-SPACE) 
       and enter yourScript.command to run the shell script, which in turn will run your Python script.

    ** Linux ** (See this link -> https://automatetheboringstuff.com/2e/appendixb/#calibre_link-683)

The generated password will follow this pattern:
Password length: 15
1 uppercase
10 lowercase
3 symbols
1 number


"""

import random, pyperclip, sys

# Character sets
uppercase = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lowercase = list("abcdefghijklmnopqrstuvwxyz")
numbers = list("0123456789")
symbols = list("!@#$%^&*")

# Constants for pattern
UPPERCASE = 1
LOWERCASE = 2
SYMBOLS = 3
NUMBERS = 4
PASSWORD_LENGTH = 15

# Function to get random character from a list
def getRandomChar(charList):
    return random.choice(charList)

# Function to generate password pattern
def generatePasswordPattern():
    passwordTemplate = {"uppercase": 0, "lowercase": 0, "symbols": 0, "numbers": 0}
    password_pattern = []
    
    while len(password_pattern) < PASSWORD_LENGTH:
        randomPatternChoice = random.randint(UPPERCASE, NUMBERS)
        if randomPatternChoice == UPPERCASE and passwordTemplate["uppercase"] < 1:
            password_pattern.append(getRandomChar(uppercase))
            passwordTemplate["uppercase"] += 1
        elif randomPatternChoice == LOWERCASE and passwordTemplate["lowercase"] < 10:
            password_pattern.append(getRandomChar(lowercase))
            passwordTemplate["lowercase"] += 1
        elif randomPatternChoice == SYMBOLS and passwordTemplate["symbols"] < 3:
            password_pattern.append(getRandomChar(symbols))
            passwordTemplate["symbols"] += 1
        elif randomPatternChoice == NUMBERS and passwordTemplate["numbers"] < 1:
            password_pattern.append(getRandomChar(numbers))
            passwordTemplate["numbers"] += 1

    return password_pattern

# Function to generate password
def generatePassword():
    password = generatePasswordPattern()
    return "".join(password)

# Main function
def main():
    # Check if the script is run from command line with arguments
    if len(sys.argv) > 1:
        print("Running in command-line mode.")
        generated_password = generatePassword()
        print("Generated Password: " + generated_password)
        pyperclip.copy(generated_password)
        print("Password copied to clipboard!")
    else:
        print("Running in interactive mode in IDE or terminal.")
        print("Welcome to the password generator program!")
        while True:
            generated_password = generatePassword()
            print("Generated Password: " + generated_password)
            pyperclip.copy(generated_password)
            print("Password copied to clipboard!")
            restart = input("Would you like to generate another password? (Y/N): ").lower()
            if restart == "n":
                print("Thanks for using the program! Enjoy your new encrypted password.")
                break
            elif restart != "y":
                print("Invalid input, please try again.")

# Run the main function
if __name__ == "__main__":
    main()
