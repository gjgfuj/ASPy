import pygame
pygame.init()
import os
import sys

import aspy.games as games
import aspy.config as config
import aspy.core as core
import aspy.game
import aspygame.game

def loop():
  game = aspy.game.game
  display = pygame.display.set_mode(game.size, game.flags)
  game.display = pygame.Surface(game.size)
  while game == aspy.game.game:
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        sys.exit(0)
      elif e.type == pygame.KEYDOWN:
        game.event(aspy.core.configparser.keydown(e), e)
      elif e.type == pygame.KEYUP:
        game.event(aspy.core.configparser.keyup(e), e)
      elif e.type == pygame.MOUSEBUTTONDOWN:
        game.event(aspy.core.configparser.mousedown(e), e)
      elif e.type == pygame.MOUSEBUTTONUP:
        game.event(aspy.core.configparser.mouseup(e), e)
    game.display.fill(game.bg)
    game.play()
    display.blit(game.display, (0,0))
    pygame.display.flip()

if __name__ == "__main__":
  aspygame.game.setup()
  while True:
    loop()
