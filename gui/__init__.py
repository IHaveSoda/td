from pygame.font import SysFont
from pygame import Rect
from pygame.draw import rect
from pygame.image import load

class GuiManager:
	def __init__(self, display, app):
		self.app = app
		self.display = display
		self.elements = []
		self.reference = {}

	def add(self, obj):
		self.elements.append(obj)
		if obj.ref is not None:
			self.reference[obj.ref] = obj # if object is to be added to self.reference

	def updatetsv(self, tsvobj):
		if type(tsvobj) == _elements.TowerSelectVertical:
			for subobj in tsvobj.grablist:
				self.app.guiobjects.append(subobj)

	def render(self):
		for element in self.elements:
			element.render(self.display)


class _elements:

	class Text:
		def __init__(self, reference, text, font="Arial", size=12, pos=[0,0]):
			self.text = text
			self.font = font
			self.size = size
			self.pos = pos
			self.upd = False
			self.ref = reference

		def render(self, display):
			display.blit(SysFont(self.font, self.size).render(str(self.text), False, (0, 0, 0)), self.pos)

	class TowerGrab:
		def __init__(self, x, y, tower, *extargs):
			self.tower = tower
			self.x = x
			self.y = y
			self.pgRect = Rect(self.x, self.y, 32, 32)
			self.img = load(self.tower.imglocation)

		def generate(self, ref):
			temp = self.tower(self.x, self.y)
			ref.towers.append(temp)
			return temp

		def render(self, display):
			display.blit(self.img, (self.x, self.y))	

	class TowerSelectVertical:
		def __init__(self, max_x, height):
			self.towerlist = []
			self.grablist = []
			self.grab_ui_offsets = []
			self.ref = "TowerSelectVertical"

			self.max_x = max_x
			self.height = height

		def createtowergrabs(self):
			y = 0
			for item in self.towerlist:
				y += 32
				self.grablist.append(_elements.TowerGrab(self.max_x-48, y, item))

		def render(self, display):
			rect(display, (211,211,211), (self.max_x-64, 0, self.max_x, self.height))
			for towerrepr in self.grablist:
				towerrepr.render(display)
