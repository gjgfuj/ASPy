import aspy.config as config
class ConfigParser:
  def fullscreen(self):
    return config.fullscreen
  def keydown(self, event):
    try:
      return config.keydown[event.key]
    except Exception:
      return ""
  def keyup(self, event):
    try:
      return config.keyup[event.key]
    except Exception:
      return ""
  def mousedown(self, event):
    try:
      return config.mousedown[event.button]
    except Exception:
      return ""
  def mouseup(self, event):
    try:
      return config.mouseup[event.button]
    except Exception:
      return ""
configparser = ConfigParser()
