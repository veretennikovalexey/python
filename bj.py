import random, sys
HEARTS = chr( 9829 )
DIAMONDS = chr( 9830 )
SPADES = chr( 9824 )
CLUBS = chr( 9827 ) 
BACKSIDE = 'backside'

def main():
  print( 'Эта игра посвящается моему сыну - Андрею' ) 

  money = 10
  while True:
    if money <= 0:
      print( 'Конец игры' )
      sys.exit()       

    print( 'Твои деньги:', money )
    bet = getBet( money )

    deck = getDeck()
    dealerHand = [ deck.pop(), deck.pop() ]
    playerHand = [ deck.pop(), deck.pop() ]

    print( 'Ставка: ', bet )
    while True: # играет игрок
      displayHands( playerHand, dealerHand, False)
      print()

      if getHandValue( playerHand ) > 21:
        break
               
      move = getMove( playerHand, money - bet ) 

      if move == '2':
        additionalBet = getBet( min( bet, ( money - bet ) ) )
        bet += additionalBet 
        print( 'Ты увеличил ставку до {}'.format( bet ) )
        print( 'Текущая ставка: ', bet )
  
      if move in ( '1', '2' ):
        newCard = deck.pop()
        rank, suit = newCard
        print( 'Твоя карта {} {}'.format( rank, suit ) )
        playerHand.append( newCard ) 
         
        if getHandValue( playerHand ) > 21:
          break

      if move in ( '0', '2' ):
        break

    if getHandValue( playerHand ) <= 21 : # у игрока меньше, чем 21 очко
      while getHandValue( dealerHand ) < 17 :
        print( 'ходит комп' )
        dealerHand.append( deck.pop() )
        displayHands( playerHand, dealerHand, False )

        if getHandValue( dealerHand ) > 21 :
          break
        input( 'нажми на клавишу enter' ) 
        print( '\n\n' )

    displayHands( playerHand, dealerHand, True )
    playerValue = getHandValue( playerHand )
    dealerValue = getHandValue( dealerHand )

    if dealerValue > 21 :
      print( 'Комп перебрал. Ты победил и выиграл {}'.format( bet ) )
      money += bet
    elif ( playerValue > 21 ) or ( playerValue < dealerValue ) :
      if playerValue > 21 :
        print( 'у тебя перебор ( очков больше, чем 21 )' )        
      print( 'комп победил' )
      money -= bet
    elif playerValue > dealerValue :
      print( 'Победа ! Ты выиграл {}'.format( bet ) )
      money += bet
    elif playerValue == dealerValue :
      print( 'ничья :)' )
      input( 'Нажми на клавишу enter' ) 
      print( '\n\n' )


def getBet( maxBet ):
  while True:
    print( 'Сколько тебе не жалко денег ( от 1 до {} )'.format( maxBet ) )
    bet = input( '> ' ).strip()
    if not bet.isdecimal():
      continue

    bet = int( bet )
    if 1 <= bet <= maxBet :
      return bet                                    # Сделать ставку


def getDeck() :
  deck = []
  for suit in ( HEARTS, DIAMONDS, SPADES, CLUBS ):
    for rank in range( 2, 11 ):
      deck.append( ( str( rank ), suit ) )
    for rank in ( 'В', 'Д', 'К', 'Т' ):
      deck.append( ( rank, suit ) )
  random.shuffle( deck )
  return deck                                       # Размешать колоду


def displayHands( playerHand, dealerHand, showDealerHand ) :
  print()
  if showDealerHand  :
    print( 'комп: ', getHandValue( dealerHand ) )
    displayCards( dealerHand )
  else :
    print( 'комп прячет одну карту' )
    displayCards( [ BACKSIDE ] + dealerHand[ 1: ] )
  print( 'игрок:', getHandValue( playerHand ) )
  displayCards( playerHand )


def getHandValue( cards ) :
  
  value = 0
  numberOfAces = 0
  
  for card in cards :
    rank = card[ 0 ]
    if rank == 'Т':
      numberOfAces += 1
    elif rank in ( 'В', 'Д', 'К' ):
      value += 10
    else:
      value += int( rank )

  value += numberOfAces 
  for ii in range( numberOfAces ) :
    if value + 10 <= 21 :
      value += 10

  return value                                      # Посчитать очки


def displayCards( cards ):
  rows = [ '', '', '', '', '' ]

  for ii, card in enumerate( cards ):
    rows[ 0 ] += ' ___  '
    if card == BACKSIDE :
      rows[ 1 ] += '|* *| '
      rows[ 2 ] += '| * | '
      rows[ 3 ] += '|___| '
    else :
      rank, suit = card
      rows[ 1 ] += '|{} | '.format( rank.ljust( 2 ) )
      rows[ 2 ] += '| {} | '.format( suit )
      rows[ 3 ] += '|_{}| '.format( rank.rjust( 2, '_' ) )

  for row in rows:
    print( row )                                   # Показать карты


def getMove( playerHand, money ):
  while True:
    moves = [ '1', '0' ]
    
    if len( playerHand ) == 2 and money > 0:
      moves.append( '2' )
      
    movePrompt = ', '.join( moves ) + '> '
    move = input( movePrompt ).upper()
    if move in ( '1', '0' ):
      return move 
    if move == '2' and '2' in moves:
      return move                                   # Ход      

if __name__ == '__main__':
  main() 

 # Запуск программы   
