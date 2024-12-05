import string, random

def generate_ps(min_length, number=True, special_character=True):      # <------ Generate a password with the specified parameters

    letter = string.ascii_letters
    digit = string.digits
    special = string.punctuation

    character=letter
    if number:
        character+=digit
    if special_character:
        character+=special

    pwd = ''
    meet_criteria = False
    has_number = False
    has_special = False

    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(character) 

        pwd+=new_char 

        if new_char in digit:
            has_number = True
        elif new_char in special:
            has_special = True

        meet_criteria = True
        if number:
            meet_criteria = has_number
        if special_character:
            meet_criteria = meet_criteria and has_special

    return pwd


#<---------- main execution ---------->

min_length = int(input('Enter the maximum length of your pwd : '))
has_number = input('Do you want have numbers in your pwd (y/n)? : ').lower() == 'y'
has_special = input('Do you want have special character in your pwd (y/n)? : ').lower() == 'y'

pwd = generate_ps(min_length, has_number, has_special)
print('The generated password is : ', pwd)
        