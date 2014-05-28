import pygame
pygame.init()
import os


import aspy.games as games
import aspygame.globalgame as globalgame

def loop():
  game = games.game
  display = pygame.display.set_mode(game.size)
  game.display = pygame.Surface(game.size)
  while True:
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        os.exit(0)
    display.fill(game.bg)
    game.play()
    display.blit(game.display (0,0))
    pygame.display.flip()

if __name__ == "__main__":
  while True:
    loop()
