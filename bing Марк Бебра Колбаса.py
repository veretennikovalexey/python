import random

# generate a random number between 123 and 789 with no repeated digits
def generate_number():
    digits = list(range(1,10)) # possible digits from 1 to 9
    number = "" # empty string to store the number
    for i in range(3): # loop three times
        digit = random.choice(digits) # choose a random digit
        number += str(digit) # append it to the number
        digits.remove(digit) # remove it from the list of possible digits
    return int(number) # return the number as an integer

# compare the user's guess with the secret number and give hints
def compare_numbers(guess, secret):
    hint = "" # empty string to store the hint
    for i in range(3): # loop three times
        if guess[i] == secret[i]: # if the digit is correct and in the right position
            hint += "Бебра " # add "Бебра" to the hint
        elif guess[i] in secret: # if the digit is correct but not in the right position
            hint += "Марк " # add "Марк" to the hint
    if hint == "": # if no digit is correct
        hint = "Колбаса" # set hint to "Колбаса"
    return hint.strip() # return hint without trailing spaces

# main program logic
secret_number = generate_number() # generate a secret number 
attempts = 20 # set maximum attempts 
while attempts > 0: # loop until attempts run out 
    print(f"Попытка {21 - attempts}:") # print current attempt 
    guess_number = input("Введите число от 123 до 987: ") # ask user for a guess
    if len(guess_number) != 3 or not guess_number.isdigit(): # check if input is valid 
        print("Неверный ввод. Попробуйте еще раз.") 
        continue 
    elif int(guess_number) < 123 or int(guess_number) > 987:
        print("Число должно быть от 123 до 987. Попробуйте еще раз.") 
        continue 
    elif len(set(guess_number)) != len(guess_number): 
        print("Число не должно содержать повторяющихся цифр. Попробуйте еще раз.") 
        continue 

    if int(guess_number) == secret_number: # check if guess is correct 
        print("Вы угадали!")  
        break  
    else:  
        print(compare_numbers(guess_number, str(secret_number)))  	# give hints based on comparison  
        attempts -= 1  	# reduce attempts by one  

if attempts == 0:  	# check if attempts are over  
    print(f"Вы проиграли. Загаданное число было {secret_number}.")
