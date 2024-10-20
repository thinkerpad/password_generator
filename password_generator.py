# INF360B - Programming in Python
# Choun Chan Nirak
# Midterm Project

"""
This is a password generator program. It will be automatically copied to your clipboard.
You can get the generated password either by running the program in an IDE
or by using the terminal command by typing the filename.

** Important Notice **
Please make sure you install the following imported libraries to ensure the program runs.

Future Improvement:
- Place the generated password in a notepad file that is saved on your desktop.

To set up typing the filename in the terminal command, follow these instructions:
    ** Windows **
    1. Create a new file in Notepad.
    2. Place this command into it:
        @py.exe C:/path_to_file/password_generator.py %*
        @pause
    3. Save it as password_generator in the C:/Windows folder.
    4. From now on, you can just run it through the command prompt by typing the filename (password_generator).
    
    ** MacOS **
    1. Create a new file in TextEdit.
    2. Place this command into it:
        #!/usr/bin/env bash
        python3 /path/to/your/pythonScript.py
    3. Save it with the .command file extension in your home folder (e.g., on my computer it’s /Users/Nirak).
    4. Open your terminal window and run this shell script:
        chmod u+x password_generator.command (This is what I named in step 3).
    5. From now on, you can just run it through the Spotlight icon (or press CMD+SPACE) 
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

# Function to get random character from the password pattern list
def getRandomChar(charList):
    return random.choice(charList)

# Function to generate password pattern, it will return a list of characters
# The reason why I don't combine generatePasswordPattern and generatePassword is because it'll be easier to change the password pattern in the future.
def generatePasswordPattern():
    passwordTemplate = {"uppercase": 0, "lowercase": 0, "symbols": 0, "numbers": 0}
    passwordPattern = []
    uppercaseLength = passwordTemplate["uppercase"]
    lowercaseLength = passwordTemplate["lowercase"]
    symbolsLength = passwordTemplate["symbols"]
    numbersLength = passwordTemplate["numbers"]
    """ 
    This loop ensures the password pattern will always follow this pattern:
        Password length: 15
        1 uppercase
        10 lowercase
        3 symbols
        1 number
    """
    while len(passwordPattern) < PASSWORD_LENGTH:
        # Randomize choice between 1-4 with each number represents the following constants: UPPERCASE = 1, LOWERCASE = 2, SYMBOLS = 3, NUMBERS = 4
        randomPatternChoice = random.randint(UPPERCASE, NUMBERS) 
        # Only adds an uppercase character if the uppercaseLength is less than 1
        if randomPatternChoice == UPPERCASE and uppercaseLength < 1:
            passwordPattern.append(getRandomChar(uppercase))
            uppercaseLength += 1
        # Only adds a lowercase character if the lowercaseLength is less than 10
        elif randomPatternChoice == LOWERCASE and lowercaseLength < 10:
            passwordPattern.append(getRandomChar(lowercase))
            lowercaseLength += 1
        # Only adds a symbol character if the symbolsLength is less than 3
        elif randomPatternChoice == SYMBOLS and symbolsLength < 3:
            passwordPattern.append(getRandomChar(symbols))
            symbolsLength += 1
        # Only adds a number character if the numberssLength is less than 1
        elif randomPatternChoice == NUMBERS and numbersLength < 1:
            passwordPattern.append(getRandomChar(numbers))
            numbersLength += 1

    return passwordPattern

# Function to generate password
def generatePassword():
    password = generatePasswordPattern()
    return "".join(password)

# Main function
def main():
    print("Running in interactive mode in IDE or terminal.")
    print("Welcome to the password generator program!")
    
    # Loop to continue if the user decides to generate another password
    while True:
        generated_password = generatePassword()
        print("Generated Password: " + generated_password)
        pyperclip.copy(generated_password)
        print("Password copied to clipboard!")
        
        # Loop to continue if the restart input is invalid
        while True:
            restart = input("Would you like to generate another password? (Y/N): ").lower()
            if restart == "n":
                print("Thanks for using the program, and don't forget to save the generated password in a secure place!")
                sys.exit()  # Exit the program
            elif restart == "y":
                break  # Valid input, exit the validation loop and generate another password
            else:
                print("Invalid input, please enter 'Y' or 'N'.")  # Prompt again if invalid


# Run the main function
if __name__ == "__main__":
    main()
