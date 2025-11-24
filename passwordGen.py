import random
import string
import secrets

def name_based_password(name, strength='easy'):
    # Basic transformations on the name
    base = name.lower()
    if strength == 'easy':
        # Shuffle letters and append a 2-digit number
        shuffled = ''.join(random.sample(base, len(base)))
        number = ''.join(random.choices(string.digits, k=2))
        return shuffled + number
    elif strength == 'strong':
        # Add uppercase, digits, and one special char
        shuffled = ''.join(random.sample(base, len(base)))
        upper = ''.join(random.choices(string.ascii_uppercase, k=2))
        digits = ''.join(random.choices(string.digits, k=3))
        special = secrets.choice(string.punctuation)
        return shuffled + upper + digits + special
    else:  # very strong
        # Mix uppercase, digits, special chars, and repeat name twice
        part1 = name.capitalize()
        part2 = ''.join(random.sample(base, len(base)))
        digits = ''.join(secrets.choice(string.digits) for _ in range(4))
        special = ''.join(secrets.choice(string.punctuation) for _ in range(2))
        return part1 + digits + special + part2 + part1

def random_password(length=12, strength='strong'):
    if strength == 'easy':
        chars = string.ascii_lowercase + string.digits
    elif strength == 'strong':
        chars = string.ascii_letters + string.digits
    else:  # very strong
        chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

def main():
    print("Password Generator")

    choice = input("Generate password based on (1) Name or (2) Random: ")
    if choice == '1':
        name = input("Enter a name to base the password on: ")
        strength = input("Choose strength (easy, strong, very strong): ").lower()
        pwd = name_based_password(name, strength)
    else:
        length = int(input("Enter desired password length: "))
        strength = input("Choose strength (easy, strong, very strong): ").lower()
        pwd = random_password(length, strength)

    print(f"Generated password: {pwd}")

if __name__ == "__main__":
    main()