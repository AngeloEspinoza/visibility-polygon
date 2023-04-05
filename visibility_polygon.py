import pygame
import environment
import robot
import sys

# Initialization 
pygame.init()

# Constants
MAP_DIMENSIONS = 642, 482

# Instantiating the environment and the robot
environment_ = environment.Environment(map_dimensions=MAP_DIMENSIONS)
robot_ = robot.Robot(start=[300, 250], radius=5, vertices=environment_.vertices)

def main():
	run = True
	clock = pygame.time.Clock()
	vertices = environment_.make_map()

	while run:
		keys = pygame.key.get_pressed()
		clock.tick(environment_.FPS) 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		# Change the robot's position with the keyboard arrows
		if keys[pygame.K_LEFT]:
			robot_.start[0] -= 3
		if keys[pygame.K_RIGHT]:
			robot_.start[0] += 3
		if keys[pygame.K_UP]:
			robot_.start[1] -= 3
		if keys[pygame.K_DOWN]:
			robot_.start[1] += 3

		# Display the robot, cast the rays, and display the visibility polygon
		robot_.draw(map=environment_.map)
		robot_.cast_rays(init=robot_.start)
		robot_.draw_visibility_polygon(map=environment_.map)
		
		# Update the frame, and restart the map again to delete previous visibility polygons
		pygame.display.update()	
		environment_.draw_walls()
		environment_.make_map()

	pygame.quit()
	sys.exit()

if __name__ == '__main__':
	main()