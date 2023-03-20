import pygame
import environment
import robot
import sys

# Initialization 
pygame.init()

# Constants
MAP_DIMENSIONS = 643, 480

# Instantiating the environment
environment_ = environment.Environment(map_dimensions=MAP_DIMENSIONS)
robot_ = robot.Robot(initial_position=(310, 250), robot_radius=5)

def main():
	run = True
	clock = pygame.time.Clock()
	vertices, rects = environment_.make_map()

	while run:
		clock.tick(environment_.FPS) 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		robot_.draw(map=environment_.map)
		points = robot_.draw_rays(vertices=vertices, obstacles=rects,
			init=robot_.initial_position, map=environment_.map)
		robot_.draw_visibility_polygon(point_cloud=points, map=environment_.map)
		pygame.display.update()	

	pygame.quit()
	sys.exit()

if __name__ == '__main__':
	main()