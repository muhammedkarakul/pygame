import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second settings
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animations')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'
catspeed = 1

# the main game loop
while True:
	DISPLAYSURF.fill(WHITE)

	if direction == 'right':
		catx += catspeed
		if catx == 280:
			direction = 'down'
	elif direction == 'down':
		caty += catspeed
		if caty == 220:
			direction = 'left'
	elif direction == 'left':
		catx -= catspeed
		if catx == 10:
			direction = 'up'
	elif direction == 'up':
		caty -= catspeed
		if caty == 10:
			direction = 'right'

	DISPLAYSURF.blit(catImg, (catx, caty))

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
