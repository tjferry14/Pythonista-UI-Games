# coding: utf-8
from random import choice
from sound import play_effect
import ui

SIGNS = ("Rock", "Paper", "Scissors") 

def player_win(player, action, computer):
	play_effect('Jump_3')
	v['game_result'].text = "Player Wins! %s %s %s." % (player, action, computer)
	
def player_loss(computer, action, player):
	play_effect('Jump_5')
	v['game_result'].text = "Computer Wins! %s %s %s." % (computer, action, player)
	
def press(sender):
	global player_choice
	player_choice = sender.title
	v['outcome'].text = player_choice
	generate_outcome()
	
def generate_outcome():
	global player_choice
	computer_choice = choice(SIGNS)
	v['cpu_outcome'].text = computer_choice

	if player_choice == computer_choice:
			play_effect('Laser_3')
			v['game_result'].text = "It's a draw! Both played %s." % (player_choice)
	elif player_choice == 'Paper' and computer_choice == 'Rock':
			player_win('Paper', 'covers', 'rock')
	elif player_choice == 'Scissors' and computer_choice == 'Paper':
			player_win('Scissors', 'cut', 'paper')
	elif player_choice == 'Rock' and computer_choice == 'Scissors':
			player_win('Rock', 'crushes', 'scissors')
	elif player_choice == 'Rock' and computer_choice == 'Paper':
			player_win('Rock', 'crushes', 'paper')

	elif computer_choice == 'Paper' and player_choice == 'Rock':
			player_loss('Paper', 'covers', 'rock')
	elif computer_choice == 'Scissors' and player_choice == 'Paper':
			player_loss('Scissors', 'cut', 'paper')
	elif computer_choice == 'Rock' and player_choice == 'Scissors':
			player_loss('Rock', 'crushes', 'scissors')
	elif computer_choice == 'Rock' and player_choice == 'Paper':
			player_loss('Rock', 'crushes', 'paper')
	else:
			v['game_result'].text = "Whoops! This wasn\'t supposed to happen!"

v = ui.load_view('rps')
v.present('sheet')
