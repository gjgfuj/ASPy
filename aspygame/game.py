import pygame
pygame.init()
import aspy.games
import aspy.loader
import aspy.game
class InitLoader(aspy.loader.Loader):
  def loadmenu(self):
    pass
  def __init__(self, menu):
    aspy.loader.Loader.__init__(self, [], menu)
class MainMenu(aspy.games.Menu):
  def startgame(self):
    print "Game Started"
  def __init__(self):
    aspy.games.Menu.__init__(self)
    self.addmenuitem("Start Game", self.startgame)
    self.addmenuitem("", self.nothing)
    self.addmenuitem("Quit", self.exit)
def setup():
  aspy.game.game = aspy.games.Load(InitLoader(MainMenu()))
