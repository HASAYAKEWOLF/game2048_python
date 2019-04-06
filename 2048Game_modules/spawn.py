#coding=utf-8

def invert(feild):
	return [row[::-1] for row in feild]

def transpose(feild):
	return [list(row) for row in zip(*feild)]

class GameFeild(object):
	def __init__(self,height=4,width=4,win=2048):
		self.height = height
		self.width = width
		self.win_value = win
		self.score = 0
		self.high_score = 0
		self.reset()

	def spawn(self):
		new_element = 4 if randrange(100) > 89 else 2
		(i,j) = choice([(i,j) for i in range(self.width) for j in range(self.height) if self.feild[i][j] == 0])
		self.feild[i][j] = new_element

	def reset(self):
		if self.score > self.high_score:
			self.high_score = self.score
		self.score = 0
		self.feild = [[0 for i in range(self.width)] for j in range(self.height)]
		self.spawn()
		self.spawn()

	def move(self, direction):
		def move_row_left(row):
			moves = {}
			moves["Left"] = lambda feild: [move_row_left(row) for row in feild]
			moves["Right"] = lambda feild: invert(moves["Left"](invert(feild)))
			moves["Up"] = lambda feild: transpose(moves["Left"](transpose(feild)))
			moves["Down"] = lambda feild: transpose(moves["Right"](transpose(feild)))

		if direction in moves:
			if self.move_is_possible(direction):
				self.feild = moves[direction](self.feild)
				self.spawn()
				return True
			else:
				return False
	def move_row_left(row):
		def tighten(row):
			new_row = [i for i in row if i != 0]
			new_row += [0 for i in range(len(row)-len(new_row))]
			return new_row

	def merge(row):
		pair = False
		new_row = []
		for i in range(len(row)):
			if pair:
				new_row.append(2*row[i])
				self.score += 2*row[i]
				pair = False
			else:
				if i+1 <len(row) and row[i] == row[i+1]:
					pair = True
					new_row.append(0)
				else:
					new_row.append(row[i])
		assert len(new_row) == len(row)
		return new_row

A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
A
A
A
A
A
A
A
A
A
A
	return tighten(merge(tighten(row)))
