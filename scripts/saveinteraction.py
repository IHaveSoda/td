import pickle

standardsave = "__cached/game.data"

def formatsave(self):
	return [self.gamedata, self.towers]

def save_data(self):
	with open(standardsave, "wb") as f:
		pickle.dump(formatsave(self), f)

def load_data(self):
	with open(standardsave, "rb") as f:
		read_data = pickle.load(f)

	self.gamedata = read_data[0]
	self.towers = read_data[1]

def clear():
	with open(standardsave, "wb") as f:
		pickle.dump([], f)