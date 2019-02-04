from pygame import Rect

class BaseTower:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.stdimg = "std"
		self.dragimg = "drag"
		self.img = self.stdimg
		self.pgRect = Rect(x, y, 32, 32)

	def update(self):
		self.pgRect = Rect(self.x, self.y, 32, 32)

	def _delete(self, app):
		for index, obj in enumerate(app.towers):
			if obj == self:
				appindex = index

		if appindex is not None:
			del app.towers[appindex]
			del self
		return

class BaseEnemy:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.img = "std"
		self.pgRect = Rect(x, y, 32, 32)

	def update(self):
		self.pgRect = Rect(self.x, self.y, 32, 32)

	def _delete(self):
		del self
