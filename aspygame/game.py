import pygame
pygame.init()
import aspy.games
import aspy.game
class InitLoader(aspy.games.Loader):
  def loadmenu(self):
    return "Menu Loaded"
  def __init__(self, menu):
    aspy.games.Loader.__init__(self, [], menu)
class MainMenu(aspy.games.Menu):
  pass
def setup():
  aspy.game.game = aspy.games.Load(InitLoader(MainMenu()))
