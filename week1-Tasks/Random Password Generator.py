import random
import string
import argparse

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_special):
    # Define character sets based on user choices
    character_sets = []
    if include_uppercase:
        character_sets.append(string.ascii_uppercase)
    if include_lowercase:
        character_sets.append(string.ascii_lowercase)
    if include_digits:
        character_sets.append(string.digits)
    if include_special:
        character_sets.append(string.punctuation)

    # If no character set is selected, default to lowercase letters
    if not character_sets:
        character_sets.append(string.ascii_lowercase)

    # Combine all selected character sets into one
    all_characters = ''.join(character_sets)

    # Generate random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description="Generate a random password with customizable length and complexity.")
    parser.add_argument('-l', '--length', type=int, default=12, help="Length of the password")
    parser.add_argument('-u', '--uppercase', action='store_true', help="Include uppercase letters")
    parser.add_argument('-lc', '--lowercase', action='store_true', help="Include lowercase letters")
    parser.add_argument('-d', '--digits', action='store_true', help="Include digits")
    parser.add_argument('-s', '--special', action='store_true', help="Include special characters")
    args = parser.parse_args()

    # Generate and print the password based on user input
    password = generate_password(args.length, args.uppercase, args.lowercase, args.digits, args.special)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
