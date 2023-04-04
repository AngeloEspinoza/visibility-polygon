import pygame
import environment
import robot
import sys

# Initialization 
pygame.init()

# Constants
MAP_DIMENSIONS = 642, 482

# Instantiating the environment
environment_ = environment.Environment(map_dimensions=MAP_DIMENSIONS)
robot_ = robot.Robot(start=(300, 250), radius=5, vertices=environment_.vertices)

def main():
	run = True
	clock = pygame.time.Clock()
	vertices = environment_.make_map()

	while run:
		clock.tick(environment_.FPS) 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		robot_.draw(map=environment_.map)
		robot_.initialize_rays(init=robot_.start)
		robot_.draw_rays(map=environment_.map)
		robot_.draw_visibility_polygon(map=environment_.map)
		robot_.draw_cloud_points(map=environment_.map)
		environment_.draw_walls()

		pygame.display.update()	

	pygame.quit()
	sys.exit()

if __name__ == '__main__':
	main()