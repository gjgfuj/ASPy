import pygame
pygame.init()
import sys
import aspy.core
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
  def loadsection(self):
    pass
class Load(Game):
  def __init__(self, loader):
    super(Load, self).__init__()
    self.size = (500,500)
    self.loader = loader
    self.font = pygame.font.SysFont("Comic Sans MS", 30)
  def play(self):
    super(Load, self).play()
    line = self.font.render(loader.loadsection(), True, (200,100,0))
    self.display.blit(self.font.render("Loading", True, (100,0,200)), (210, 30))
    self.display.blit(line, (250-line.get_width/2, 100))
game = Game()
