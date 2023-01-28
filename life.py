import time
import pygame
import random

def ld( _, index, kk ):           # life or death
  x = index %  kk
  y = index // kk
  nn = 0
  ss = 0
  x1 = x - 1 # сосед слева 
  if x1 < 0:
    x1 = x1 + kk
  ss = ss + _[ y * kk + x1 ]   
  x2 = x + 1 # сосед справа
  if x2 == kk:
    x2 = x2 - kk
  ss = ss + _[ y * kk + x2 ]   
  y1 = y - 1 # сосед сверху 
  if y1 < 0:
    y1 = y1 + kk
  ss = ss + _[ y1 * kk + x ]     
  y2 = y + 1 # сосед снизу
  if y2 == kk:
    y2 = y2 - kk
  ss = ss + _[ y2 * kk + x ]         
  ss = ss + _[ y1 * kk + x1 ]   # сосед слева  сверху 
  ss = ss + _[ y1 * kk + x2 ]   # сосед справа сверху 
  ss = ss + _[ y2 * kk + x1 ]
  ss = ss + _[ y2 * kk + x2 ]
   
  if _[ index ] == 0 and ss == 3:
    nn = 1
  if _[ index ] == 1 and ss == 2:
    nn = 1
  if _[ index ] == 1 and ss == 3:
    nn = 1
  # print( ss )  
  return nn # 1 или 0   

def xy( index, kk ):
  x = index %  kk * 20 + 10
  y = index // kk * 20 + 10
  return( ( x, y ) )  

kk = 50 # сторона квадрата
white = ( 255, 255, 255 )
black = ( 0, 0, 0 )

sc = pygame.display.set_mode( ( kk * 20, kk * 20 ) )

_ = []             # список

for ii in range( 0, kk * kk ) :
  _.append( random.randint( 0, 1 ) * random.randint( 0, 1 ) )

while True:
  for ii in pygame.event.get() :
    if ii.type == pygame.QUIT :
      pygame.quit()    

  for ii in range( 0, kk * kk ) :    
    if _[ ii ] == 1:
      pygame.draw.circle( sc, white, xy( ii, kk ), 10 )
    else:
      pygame.draw.circle( sc, black, xy( ii, kk ), 10 )

  pygame.display.update()

  time.sleep( 0.08 )

  _2 = []
  for ii in range( 0, kk * kk ) :
    _2.append( ld( _, ii, kk ) )

  _ = _2  
