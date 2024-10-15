import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidField import *


def main():
	pygame.init()
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill(pygame.Color('black'))
		for drawable_item in drawable:
			drawable_item.draw(screen)
		dt = clock.tick(60) / 1000
		for updatable_item in updatable:
			updatable_item .update(dt)
		for asteroid in asteroids:
			if asteroid.is_colliding(player) == True:
				print("Game over!")
				sys.exit()
		pygame.display.flip()
		
		
		

if __name__ == "__main__":
	main()
