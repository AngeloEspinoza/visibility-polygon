import pygame
import environment
import sys

# Initialization 
pygame.init()

# Constants
MAP_DIMENSIONS = 640, 480

# Instantiating the environment
environment_ = environment.Environment(map_dimensions=MAP_DIMENSIONS)

def main():
	run = True
	clock = pygame.time.Clock()
	environment_.make_map()

	while run:
		clock.tick(environment_.FPS) 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		pygame.display.update()	

	pygame.quit()
	sys.exit()

if __name__ == '__main__':
	main()