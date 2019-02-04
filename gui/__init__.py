from pygame import Rect

class GuiManager:
	def __init__(self, app, display):
		self.app = app
		self.display = display
		self.elements = []

	def add(self, obj): 
		self.elements.append(obj)
		if type(obj) in interactables:
			self.app.guiobjects.append(obj)

	def add_render_order(self):
		for obj in self.elements:
			self.app.game_renderer.add(obj)

class Text:
	def __init__(self, text, x, y):
		self.img = "_rect"

		self.text = text
		self.x = x 
		self.y = y

class Box:
	def __init__(self, x, y, w, h, colour=(0,0,0)):
		self.img = "_rect"
	
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.col = colour

class TowerGrabTile:
	def __init__(self, tower, img, x, y):
		self.img = img

		self.tower = tower
		self.x = x
		self.y = y
		self.pgRect = Rect(self.x, self.y, 32, 32)

	def generate(self, app):
		temp = self.tower(self.x, self.y)
		app.towers.append(temp)
		return temp

class Button:
	pass

class EfficientText:
	pass


interactables = [TowerGrabTile]