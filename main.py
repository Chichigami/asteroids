import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from pewpew import Shot
import sys

def main():
	pygame.init()
	decouple = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
 
	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	bullets = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updateable, drawable)
	Player.containers = (updateable, drawable)
	AsteroidField.containers = (updateable)
	Shot.containers = (bullets, updateable, drawable)
	field = AsteroidField()

	#init
	user = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

	#gameplay loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		for i in updateable:
			i.update(dt)
		
		for asteroid in asteroids:
			if asteroid.collision(user):
				print("Game Over!")
				sys.exit()

			for bullet in bullets:
				if asteroid.collision(bullet):
					asteroid.split()
					bullet.kill()


		screen.fill(color="black")

		for j in drawable:
			j.draw(screen)

		pygame.display.flip()

		dt = decouple.tick(144)/1000

if __name__ == "__main__":
	main()
