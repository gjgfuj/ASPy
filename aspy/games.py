import pygame
pygame.init()
import sys
import aspy.core
import time
class Game:
  def __init__(self):
    self.size = (100,100)
    self.bg = (0,0,0)
    self.flags = 0
    if aspy.core.configparser.fullscreen():
      self.flags |= pygame.FULLSCREEN
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
class Loader:
  def __init__(self, listofloadfuncs, endgame):
    self.f = listofloadfuncs
    self.endgame = endgame
    self.ended = False
  def loadsection(self):
    if self.ended:
      time.sleep(1)
      aspy.game.game = self.endgame
    try:
      return self.f.pop(0)()
    except IndexError:
      self.ended = True
      return "Loaded."
class TestLoader(Loader):
  def loada(self):
    time.sleep(1)
    return "Loaded A"
  def loadb(self):
    time.sleep(2)
    return "Loaded B"
  def loadc(self):
    time.sleep(0.5)
    return "C Loaded"
  def __init__(self, endgame):
    Loader.__init__(self, [self.loada, self.loadc, self.loada, self.loadb, self.loadc], endgame)
class Load(Game):
  def __init__(self, loader):
    Game.__init__(self)
    self.size = (500,500)
    self.bg = (255,50,0)
    self.loader = loader
    self.font = pygame.font.SysFont("Comic Sans MS", 30)
  def play(self):
    Game.play(self)
    line = self.font.render(self.loader.loadsection(), True, (200,150,0))
    self.display.blit(self.font.render("Loading", True, (100,0,200)), (210, 30))
    self.display.blit(line, (250-line.get_width()/2, 400))
