import re

def check_length(password):
    return len(password) >= 8

def check_uppercase(password):
    return any(char.isupper() for char in password)

def check_lowercase(password):
    return any(char.islower() for char in password)

def check_digit(password):
    return any(char.isdigit() for char in password)

def check_special_char(password):
    special_chars = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    return special_chars.search(password) is not None

def assess_strength(password):
    criteria = {
        'length': check_length(password),
        'uppercase': check_uppercase(password),
        'lowercase': check_lowercase(password),
        'digit': check_digit(password),
        'special_char': check_special_char(password)
    }

    score = sum(criteria.values())
    strength = ''

    if score == 5:
        strength = 'very strong'
    elif score >= 4:
        strength = 'strong'
    elif score >= 3:
        strength = 'moderate'
    elif score >= 2:
        strength = 'weak'
    else:
        strength = 'very weak'

    return strength

def main():
    password = input("Enter your password: ")
    
    strength = assess_strength(password)
    
    print("Password strength:", strength)
    
if __name__ == "__main__":
    main()
