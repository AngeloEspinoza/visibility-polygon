import pygame
import environment
import robot
import argparse
import sys

# Command line arguments
parser = argparse.ArgumentParser(description='Implements the visibility polygon algorithm for a \
	point.')
parser.add_argument('-st', '--start', nargs='+', type=int, metavar='', required=False,
	default=[300, 250], help='Initial position of the robot in X and Y, respectively')
parser.add_argument('-sr', '--show_rays', type=bool, action=argparse.BooleanOptionalAction, 
	metavar='', required=False, help='Show only the casted rays on screen')
args = parser.parse_args()

# Initialization 
pygame.init()

# Constants
MAP_DIMENSIONS = 642, 482

# Instantiating the environment and the robot
environment_ = environment.Environment(map_dimensions=MAP_DIMENSIONS)
robot_ = robot.Robot(start=args.start, radius=5, vertices=environment_.vertices)

def main():
	run = True
	clock = pygame.time.Clock()
	vertices = environment_.make_map()

	if environment_.get_position_color(robot_.start) == environment_.WHITE:
		raise Exception('Invalid start, robot out of bounds. Try again')

	while run:
		keys = pygame.key.get_pressed()
		
		clock.tick(environment_.FPS) 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		if keys[pygame.K_LEFT]:
			robot_.position[0] -= 3
			surface_color = environment_.get_position_color(robot_.position)

			if surface_color != robot_.GRAY:
				robot_.position[0] += 3
		
		elif keys[pygame.K_RIGHT]:
			robot_.position[0] += 3
			surface_color = environment_.get_position_color(robot_.position)

			if surface_color != robot_.GRAY:
				robot_.position[0] -= 3
		
		elif keys[pygame.K_UP]:
			robot_.position[1] -= 3
			surface_color = environment_.get_position_color(robot_.position)

			if surface_color != robot_.GRAY:
				robot_.position[1] += 3

		elif keys[pygame.K_DOWN]:
			robot_.position[1] += 3
			surface_color = environment_.get_position_color(robot_.position)

			if surface_color != robot_.GRAY:
				robot_.position[1] -= 3

		# Display the robot, cast the rays, and display the visibility polygon
		robot_.draw(map=environment_.map)
		robot_.cast_rays(init=robot_.start)

		if args.show_rays:
			robot_.draw_rays(map=environment_.map)
		elif not args.show_rays:
			robot_.draw_visibility_polygon(map=environment_.map)

		# Update the frame, and restart the map again to delete previous visibility polygons
		pygame.display.update()	
		environment_.make_map()

	pygame.quit()
	sys.exit()

if __name__ == '__main__':
	main()