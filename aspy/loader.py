import aspy.game
import time
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
