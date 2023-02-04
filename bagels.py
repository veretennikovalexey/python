import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
  print( 'Перевод программы Эла bagels.py' )
  print( )
  print( '******************************' )
  print( 'Эта программа посвящается моему сыну, Андрею !' )
  print( '******************************' )
  print( 'Привет, Андрей !' )
  while True :
    secretNum = getSecretNum()
    print( 'Я задумал число' )
    print( 'У тебя {} попыток'.format( MAX_GUESSES ) )

    numGuesses = 1
    while numGuesses <= MAX_GUESSES : 
      guess = ''
      while len( guess ) != NUM_DIGITS or not guess.isdecimal():
        print( 'Guess #{}: '.format( numGuesses ) )   
        guess = input( '> ' )
      
      clues = getClues( guess, secretNum )
      print( clues )
      numGuesses += 1

      if guess == secretNum:
        break
      if numGuesses > MAX_GUESSES:
        print( 'Охххх.....' )
        print( 'Я загадал число {}'.format( secretNum ) )         
    
    print( 'Ещё раз ? ( нажми 1 если Да и затем нажми enter )' )
    if not input( '> ' ).startswith( '1' ):
      break
  print( 'Спасибо за игру. Мой сладкий Пупсик. Люблю тебя' )

def getSecretNum():
  numbers = list( '0123456789' )
  random.shuffle( numbers )
  secretNum = ''
  for ii in range( NUM_DIGITS ):
    secretNum += str( numbers[ ii ] )
  return secretNum

def getClues( guess, secretNum ):
  if guess == secretNum:
    return 'Правильно !'

  clues = [] 

  for ii in range( len( guess ) ):
    if guess[ ii ] == secretNum[ ii ]:
      clues.append( 'Марк' ) # цифра стоит на своём месте 
    elif guess[ ii ] in secretNum:
      clues.append( 'Бебра' )
  
  if len( clues ) == 0:
    return 'Колбаса'
  else:
    clues.sort()
    return ' '.join( clues ) 


if __name__ == '__main__':
  main()  


'''
'''