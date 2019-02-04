from pygame import constants as pgc
from pygame.mouse import get_pos
from scripts.saveinteraction import save_data
import TDObjects

offsets = []
holding_active = False

def check_keyboard_input(app, event):
	if event.type == pgc.KEYDOWN:
		if event.key == pgc.K_F12:
			save_data(app)
			print("Saved game!")

def check_mouse_click(app):
	global offsets
	global holding_active

	mouse = get_pos()
	for event in app.events:
		check_keyboard_input(app, event)

		if event.type == pgc.QUIT: return True

		if event.type == pgc.MOUSEBUTTONDOWN and event.button == 1:
			if app.selected is None:
				for element in app.guiobjects:
					if element.pgRect.collidepoint(mouse):
						app.selected = element.generate(app)
						app.selected.img = app.selected.dragimg
						offsets = [mouse[0]-element.x, mouse[1]-element.y]
						holding_active = True
						return 

			undermouse = None # tower
			for tower in app.towers:
				if tower.pgRect.collidepoint(mouse):
					undermouse = tower

			if undermouse is not None:
				if holding_active and app.selected is not None:
					app.selected.x = mouse[0] - offsets[0]
					app.selected.y = mouse[1] - offsets[1]
					app.selected.update()
					app.selected.img = app.selected.stdimg
					app.selected = None
					holding_active = False
					return 

				elif not holding_active and app.selected is None:
					app.selected = undermouse
					app.selected.img = app.selected.dragimg
					offsets = [mouse[0]-undermouse.x, mouse[1]-undermouse.y]
					holding_active = True
					return 

		elif event.type == pgc.MOUSEBUTTONDOWN and event.button == 3:
			for tower in app.towers:
				if tower.pgRect.collidepoint(mouse):
					tower._delete(app)
					return

		else:
			if holding_active: 
				app.selected.x = mouse[0] - offsets[0]
				app.selected.y = mouse[1] - offsets[1]
				app.selected.update()