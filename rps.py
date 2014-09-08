from random import choice
import ui

SIGNS = ("Rock", "Paper", "Scissors") 
VERBS = ("crushes", "covers", "cut") 
	
def press(sender):
	global player_choice
	player_choice = sender.title
	v['outcome'].text = player_choice
	generate_outcome()
	
def generate_outcome():
	global player_choice
	computer_choice = choice(SIGNS)
	v['cpu_outcome'].text = computer_choice
	if player_choice > computer_choice:
			verb = VERBS[SIGNS.index(player_choice)]
			v['game_result'].text = "Player wins: %s %s %s." % (player_choice, verb, computer_choice)
	elif player_choice == computer_choice:
			v['game_result'].text = "It's a draw! Both played %s." % (player_choice)
	else:
			verb = VERBS[SIGNS.index(computer_choice)]
			v['game_result'].text = "Player lost: %s %s %s." % (computer_choice, verb, player_choice)

v = ui.load_view('rps')
v.present('sheet')
