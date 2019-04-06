#coding=utf-8

def main(stdscr):

	def init():
		return "Game"

	def not_game(state):
		response = defaultdict(lambda: state)
		response["Restart"],response["Exit"] = "Init", "Exit"
		return response[action]

	def game():
		if action == "Restart":
			return "Init"
		if action == "Exit":
			return "Exit"
		if action == "Win":
			return "Win"
		if action == "GameOver":
			return "GameOver"
		return "Game"

	state_actions = {"Init":init, "Win":lambda:not_game("Win"), "GameOver": lambda:not_game("GameOver"), "Game": game}
	state = "Init"

	while state != "Exit":
		state = state_actions[state]()	
