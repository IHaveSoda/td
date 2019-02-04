import pickle
import os

standardsave = "__cached/game.data"

def check_save_exists():
	if os.path.exists("__cached/game.data"):
		pass
	else:
		with open("__cached/game.data", "w") as f:
			f.write("")



def formatsave(self):
	return [self.gamedata, self.towers]

def save_data(self):
	check_save_exists()
	with open(standardsave, "wb") as f:
		pickle.dump(formatsave(self), f)

def load_data(self):
	check_save_exists()
	with open(standardsave, "rb") as f:
		read_data = pickle.load(f)

	self.gamedata = read_data[0]
	self.towers = read_data[1]

def clear():
	check_save_exists()
	with open(standardsave, "wb") as f:
		pickle.dump([], f)