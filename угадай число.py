import random

def угадай():
    while True:
        число = input( '> ' )
        if число.isdecimal():
            return int( число )
        print( 'Введите число от 1 до 100' )

print( 'Угадайте число' )
print()

загаданное_число = random.randint( 1, 100 )

print( 'Я загадал число от 1 до 100' )

for ii in range( 10 ):
    print( 'Количество попыток', str( 10 - ii ) )
    число = угадай()
    if число == загаданное_число :
        break
    if число < загаданное_число :
        print( 'больше' )
    if число > загаданное_число :
        print( 'меньше' )

if число == загаданное_число :
    print( 'Вы угадали !' )
else :
    print( 'Увы. Заданное число = ', загаданное_число )    

'''
Программа угадай число
'''
































