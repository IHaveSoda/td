from pygame import Rect

class BaseTower:
	imglocation = "resources/media/visual/sprites/tile.png"

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.stdimg = "missingtile"
		self.dragimg = "redmissingtile"
		self.img = self.stdimg

		self.pgRect = Rect(x, y, 32, 32)
		self.dragged = False

	def update(self):
		self.pgRect = Rect(self.x, self.y, 32, 32)

	def _delete(self, app):
		for index, obj in enumerate(app.towers):
			if obj == self:
				ind = index

		if ind is not None:
			del app.towers[ind]
			del self
			return