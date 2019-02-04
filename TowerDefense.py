import pygame
import pickle
import sys

import scripts.saveinteraction
import scripts.mouseevents
import gui
import TDObjects

WIN_SIZE = [700,500]
FRAMES = 60

GAME_DEF_AREA = [0, 0, 636, 500]

class Renderer:
	def __init__(self, app, display):
		self.app = app
		self.stack = []
		self.display = display

	def _nullfunction(self, *a, **kw): pass
	def add(self, obj): self.stack.append(obj)
	def reset(self): self.stack = []
	def render(self): 
		self.display.fill((255,255,255))
		for obj in self.stack:
			d = {TDObjects.BaseTower: lambda: self.display.blit(self.app.images[obj.img], (obj.x, obj.y)), # tower rendering

				TDObjects.BaseEnemy: lambda: self._nullfunction(), # enemy rendering
				
				gui.TowerGrabTile: lambda: self.display.blit(self.app.images[obj.img], (obj.x, obj.y)) # gui rendering

				}.get(type(obj), self._nullfunction)()
		self.reset()

	

class App:
	def __init__(self):
		# python / pygame setup
		pygame.init()
		pygame.display.set_caption("TowerDefense")
		self.display = pygame.display.set_mode(WIN_SIZE)
		self.clock = pygame.time.Clock()
		self.overlay = gui.GuiManager(self, self.display)
		self.game_renderer = Renderer(self, self.display)

		# function definitions
		def _addtower(c, *args, **kwargs): 
			tempobj = c(*args, **kwargs)
			self.towers.append(tempobj)
			self.game_renderer.add(tempobj)
		def _add_towers_to_render_order(self): 
			for tower in self.towers:
				self.game_renderer.add(tower)

		# data setup
		self.images = {
			"std":			pygame.image.load("resources/media/visual/sprites/tile.png"),
			"drag":			pygame.image.load("resources/media/visual/sprites/redtile.png"),
			"kommando":		pygame.image.load("resources/media/visual/sprites/kommando.png"),
			"robo":			pygame.image.load("resources/media/visual/sprites/bigbois_robo.png"),

			"_icon":	pygame.image.load("resources/media/visual/TowerDefense.png"),
			"_rect":	"Should draw pygame.rect from **args (in self.game_renderer.add)."
			}

		self.gamedata = {"wave":0, 
				   "money":0, 
				   "map":"resources/maps/testing.json",
				   "difficutly":"easy"}

		self.towers = []
		self.guiobjects = []
		
		# tower debug
		#_addtower(TDObjects.BaseTower, 0, 0)
		#scripts.saveinteraction.save_data(self)
		#scripts.saveinteraction.clear()

		# misc.
		self.selected = None
		scripts.saveinteraction.load_data(self)

		pygame.display.set_icon(self.images["_icon"])
		self.overlay.add(gui.TowerGrabTile(TDObjects.BaseTower, "std", 0, 0))

		

		# mainloop
		while True:
			self.clock.tick(FRAMES)
			pygame.event.pump()
			self.events = pygame.event.get()
			break_loop = scripts.mouseevents.check_mouse_click(self)
			if break_loop: 
				break

			_add_towers_to_render_order(self)
			self.overlay.add_render_order()
			self.game_renderer.render()

			pygame.display.update()
			

		# save, quit pygame, close app
		scripts.saveinteraction.save_data(self)
		pygame.quit()
		sys.exit()

if __name__ == "__main__":
	cb = App()