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
class Menu(Game):
  def __init__(self):
    Game.__init__(self)
    self.size = (500,600)
    self.bg = (60,200,40)
    self.menuitemorder = []
    self.menuitems = {}
    self.menuitemrects = {}
    self.font = pygame.font.SysFont("Cambria", 30)
  def addmenuitem(self, name, action):
    self.menuitemorder.append(name)
    self.menuitems[name] = action
  def exit(self):
    sys.exit(0)
  def nothing(self):
    pass
  def select(self, pos):
    Game.select(self, pos)
    for i in self.menuitemrects:
      if pygame.Rect(self.menuitemrects[i]).collidepoint(pos):
        self.menuitems[i]()
  def play(self):
    Game.play(self)
    y = 100
    for i in self.menuitemorder:
      if i in self.menuitemrects:
        self.display.blit(self.font.render(i, True, (10,20,200), self.menuitemrects[i]))
      else:
        rendered = self.font.render(i, True, (10,20,200))
        self.menuitemrects[i] = (self.size[0]/2-rendered.get_width()/2, y, rendered.get_width(), rendered.get_height())
      y += 50
