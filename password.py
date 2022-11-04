import random

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
           "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

total_length = num_letters + num_symbols + num_numbers

password = ""

while len(password) < total_length:
    type_selector = random.randint(0, 2)

    if type_selector == 0 and num_letters > 0:
        rand_int = random.randint(0, len(letters) - 1)
        password += letters[rand_int]
        num_letters -= 1
    elif type_selector == 1 and num_numbers > 0:
        rand_int = random.randint(0, len(numbers) - 1)
        password += numbers[rand_int]
        num_numbers -= 1
    elif type_selector == 2 and num_symbols > 0:
        rand_int = random.randint(0, len(symbols) - 1)
        password += symbols[rand_int]
        num_symbols -= 1

print(password)
