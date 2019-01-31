import pygame
import pickle
import sys

import scripts.saveinteraction
import scripts.mouseevents
import gui
import TDObjects

WIN_SIZE = [700,500]
FRAMES = 60

class App:
	def __init__(self):
		# python / pygame setup
		pygame.init()
		pygame.display.set_caption("TowerDefense")
		self.display = pygame.display.set_mode(WIN_SIZE)
		self.clock = pygame.time.Clock()
		self.overlay = gui.GuiManager(self.display, self)

		# function definitions
		def _addtower(c, *args, **kwargs): self.towers.append(c(*args, **kwargs))
		def _render(self, obj): self.display.blit(self.images[obj.img], (obj.x, obj.y))

		# data setup
		self.images = {
						"missingtile":		pygame.image.load("./resources/media/visual/sprites/tile.png"),
						"redmissingtile":	pygame.image.load("./resources/media/visual/sprites/redtile.png"),
					  }
		self.gamedata = {"wave":0, "money":0}
		self.towers = []
		self.guiobjects = []
		scripts.saveinteraction.load_data(self)

		# misc.
		self.selected = None
		self.overlay.add(gui._elements.TowerSelectVertical(WIN_SIZE[0], WIN_SIZE[1]))
		self.overlay.add(gui._elements.Text("fps", self.clock.get_fps()))
		
		self.overlay.reference["TowerSelectVertical"].towerlist.append(TDObjects.BaseTower)
		self.overlay.reference["TowerSelectVertical"].createtowergrabs()
		self.overlay.updatetsv(self.overlay.reference["TowerSelectVertical"])

		

		# mainloop
		while True:
			self.clock.tick(FRAMES)
			pygame.event.pump()
			self.events = pygame.event.get()

			break_loop = scripts.mouseevents.check(self)
			if break_loop: break

			self.overlay.reference["fps"].text = self.clock.get_fps()
			self.display.fill((255,255,255))
			for tower in self.towers:
				_render(self, tower)
			self.overlay.render()

			pygame.display.update()
			

		# save, quit pygame, close app
		scripts.saveinteraction.save_data(self)
		pygame.quit()
		sys.exit()

if __name__ == "__main__":
	cb = App()