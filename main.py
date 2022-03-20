import pygame
from pygame.locals import *
import pickle
from os import path

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

background_img = pygame.transform.scale(pygame.image.load('background - Copy.jpg'), (800,800))
party_hat_btn_img = pygame.image.load('PARTYHAT - Copy.png')
pirate_hat_btn_img = pygame.image.load('PIRATEHAT - Copy.png')
sombrero_btn_img = pygame.image.load('SOMBRERO - Copy.png')
top_hat_btn_img = pygame.image.load('TOPHAT - Copy.png')
start_btn_img = pygame.transform.scale(pygame.image.load('STARTBTN.png'),(150,80))
exit_btn_img = pygame.transform.scale(pygame.image.load('EXISTBTN.png'),(150,80))

class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.clicked = False

	def draw(self):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False


		#draw button
		screen.blit(self.image, self.rect)

		return action
start_button = Button(screen_width // 2 - 350, screen_height // 2, start_btn_img)
exit_button = Button(screen_width // 2 + 150, screen_height // 2, exit_btn_img)


run = True
main_menu = True
game_play = False
while run:

	clock.tick(fps)

	if main_menu == True:
		if exit_button.draw():
			run = False
		if start_button.draw():
			main_menu = False
			game_play = True



	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()