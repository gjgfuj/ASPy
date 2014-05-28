import pygame
pygame.init()
import sys
class Game:
  def __init__(self):
    self.size = (100,100)
    self.bg = (0,0,0)
  def play(self):
    pass
  def select(self, pos):
    pass
  def context(self, pos):
    pass
  def event(self, event, oevent):
    if event == "exit":
      sys.exit(0)
    if event == "select":
      self.select(oevent.pos)
    if event == "context":
      self.context(oevent.pos)
game = Game()
