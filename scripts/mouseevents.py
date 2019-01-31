from pygame import constants as pgc
from pygame.mouse import get_pos
import TDObjects
from gui import _elements

def check(app):
	if app.selected is None:
		for event in app.events:
			if event.type == pgc.QUIT: return "break loop"

			mousepos = get_pos()
			undermouse = None
			for tower in app.towers:
				if tower.pgRect.collidepoint(mousepos):
					undermouse = tower
					break

			if undermouse is None:
				for obj in app.guiobjects:
					if obj.pgRect.collidepoint(mousepos):
						undermouse = obj
						break

			if (event.type == pgc.MOUSEBUTTONDOWN and event.button == 1) and type(undermouse) == _elements.TowerGrab:
				app.selected = undermouse.generate(app)
				print("got grab")
				if app.selected is not None:
					app.selected.img = app.selected.dragimg
					app.selected.dragged = True
					MovingObj.objapp = app.selected
					MovingObj.offsets = [int(mousepos[0]-app.selected.x), int(mousepos[1]-app.selected.y)]
					return

			elif event.type == pgc.MOUSEBUTTONDOWN and event.button == 3:
					if tower.pgRect.collidepoint(mousepos):
						tower._delete(app)

			elif event.type == pgc.MOUSEBUTTONDOWN and event.button == 1:
				app.selected = undermouse
				if app.selected is not None:
					app.selected.img = app.selected.dragimg
					app.selected.dragged = True
					MovingObj.objapp = app.selected
					MovingObj.offsets = [int(mousepos[0]-app.selected.x), int(mousepos[1]-app.selected.y)]
					return

	if app.selected is not None:
		for event in app.events:
			if event.type == pgc.MOUSEBUTTONUP and event.button == 1:
				app.selected.img = app.selected.stdimg
				app.selected.update()
				app.selected = None
				MovingObj.objapp = None
				return

		MovingObj.update()

	else:
		pass



class MovingObj:
	objapp = None
	offsets = []

	def update():
		if MovingObj.objapp is not None:
			mousepos = get_pos()
			MovingObj.objapp.x = mousepos[0] - MovingObj.offsets[0]
			MovingObj.objapp.y = mousepos[1] - MovingObj.offsets[1] 
			