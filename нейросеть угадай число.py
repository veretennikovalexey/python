import random

print("Привет! Давай поиграем в игру 'Угадай число'!")
print("Я загадываю число от 1 до 100, а ты должен угадать его за не более чем 10 попыток.")

number = random.randint(1, 100)
tries = 0

while tries < 10:
    tries += 1
    print(f"Попытка номер {tries}")
    guess = input("Какое число я загадал? ")
    
    if not guess.isdigit():
        print("Некорректный ввод. Пожалуйста, введите целое число.")
        continue
        
    guess = int(guess)
    
    if guess < number:
        print("Мое число больше.")
    elif guess > number:
        print("Мое число меньше.")
    else:
        print(f"Поздравляю! Ты угадал мое число за {tries} попыток!")
        break

if tries == 10:
    print(f"К сожалению, ты не угадал мое число за {tries} попыток. Я загадал число {number}.")
