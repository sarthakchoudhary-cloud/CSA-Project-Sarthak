# Custom Password Generator

This Python program generates passwords with three levels of strength (easy, strong, very strong). It supports generating passwords based on a user-provided name or as completely random passwords.

## Features

- **Name-based passwords:** Creates passwords inspired by a given name, with varying complexity.
- **Random passwords:** Generates secure random passwords of a specified length.
- **Strength levels:** Easy, strong, and very strong password options.
- **Three imports used:** Utilizes `random`, `string`, and `secrets` for randomness and character handling.
- **Cryptographically secure randomness:** Uses `secrets` module for generating secure passwords.

## Password Strength Criteria

- Easy: Simple transformations or random choices with lowercase and digits.
- Strong: Mix of uppercase, lowercase, digits, sometimes special characters.
- Very Strong: Complex combination of uppercase, lowercase, digits, and multiple special characters.

## How to Use

1. Run the program.
2. Choose to generate a password based on (1) Name or (2) Random.
3. If name-based, enter your name and choose strength level.
4. If random, input desired password length and choose strength level.
5. View the generated password.

## Example Output