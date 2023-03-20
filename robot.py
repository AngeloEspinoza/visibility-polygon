import pygame
import math

class Robot():
	"""
	A class for the holonomic robot.

	Attributes
	----------

	"""
	def __init__(self, initial_position, robot_radius):
		# Colors 
		self.WHITE = (255, 255, 255)
		self.BLACK = (0, 0, 0)
		self.RED = (255, 0, 0)
		self.GREEN = (0, 255, 0)
		self.BLUE = (0, 0, 255)
		self.BROWN = (189, 154, 122)
		self.GRAY = (105, 105, 105)
		self.YELLOW = (255, 255, 0)

		# Robot settings
		self.initial_position = initial_position
		self.robot_radius = robot_radius

	def draw(self, map):
		"""Draws the robot on map.
		
		Parameters
		----------
		map : pygame.Surface
			The where the robot will be drawn.
		"""
		pygame.draw.circle(surface=map, color=self.BLACK,
		 	center=self.initial_position, radius=self.robot_radius)
		
		pygame.draw.circle(surface=map, color=self.GREEN,
		 	center=(100, 100), radius=self.robot_radius)

	def interpolation(self, p1, p2):
		"""Interpolates a line.

		Given an ordered pair of initial point p1 and an 
		end point p2, it computes points between p1 and p2. 

		Parameters
		----------
		p1 : tuple 
			Initial Point.
		p2 : tuple 
			End Point.

		Returns
		-------
		list
			Coordinates of the points resulted by the interpolation.
		"""
		p11, p12 = p1[0], p1[1]
		p21, p22 = p2[0], p2[1]
		coordinates = []

		for i in range(0, 401):
			u = i / 400
			x = p11 * u + p21 * (1 - u)
			y = p12 * u + p22 * (1 - u)
			coordinates.append((x, y))

		return coordinates

	def euclidean_distance(self, p1, p2):
		"""Euclidean distance between two points.

		Parameters
		----------
		p1 : int
			Start point.
		p2 : int 
			End point.

		Returns
		-------
		float
			Euclidean distance metric.
		"""
		return int(math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2))

	def get_line_angle(self, p1, p2):
		"""Gets the angle of a given line.

		Given the start point and the point of the line, it 
		computes the angle of such line.

		Parameters
		----------
		p1 : int
			Start point.
		p2 : int 
			End point.

		Returns
		-------
		float
			Angle of the line.
		"""
		dx = p2[0] - p1[0]
		dy = p2[1] - p1[1]
		rads = math.atan2(dy, dx)
		rads %= 2*math.pi
		degs = math.degrees(rads)

		return rads

	def draw_visibility_polygon(self, point_cloud, map):
		"""Draws the visibility polygon given a set of points."""
		ordered_points = []
		for point in point_cloud:
			angle = self.get_line_angle(self.initial_position, point)
			ordered_points.append((angle, point))
		
		ordered_points.sort()
		ordered_points = [point[1] for point in ordered_points]
		pygame.draw.polygon(surface=map, color=self.YELLOW,
			points=ordered_points)
		self.draw(map=map)


	def draw_rays(self, vertices, obstacles, map, init):
		"""Draws a raytracing from the robot's position.

		Parameters
		----------
		vertices : tuple
			Vertices of the map corners.
		obstacles : pygame.Rect 
			Rectangle obstacle.
		map : pygame.Surface
			Environment to draw on.
		init : tuple
			Initial robot's position.

		Returns
		-------
		None
		"""
		left_distances = []
		right_distances = []
		all_distances = []
		offset = 0.01
		dst_offset = 500
		visibility_points = []

		for vertice in vertices:
			angle = self.get_line_angle(init, vertice)
			angle_left = angle - offset
			angle_right = angle + offset
			angle_left %= math.pi * 2
			angle_right %= math.pi * 2

			dst = self.euclidean_distance(init, vertice)
			left_offset = tuple([init[0] + (dst_offset + dst) 
				* math.cos(angle_left), init[1] + (dst_offset + dst)
				* math.sin(angle_left)])
			right_offset = tuple([init[0] + (dst_offset + dst) 
				* math.cos(angle_right), init[1] + (dst_offset + dst)
				* math.sin(angle_right)])

			# Left and right rays interpolation
			left_interpolation = self.interpolation(self.initial_position, left_offset)
			right_interpolation = self.interpolation(self.initial_position, right_offset)

			for left, right in zip(left_interpolation, right_interpolation):
				for rect in obstacles:
					left_ray_collision = rect.collidepoint(left)
					right_ray_collision = rect.collidepoint(right)

					if left_ray_collision:
						left_distance = self.euclidean_distance(init, left)
						left_distances.append((left_distance, left))
					
					if right_ray_collision:
						right_distance = self.euclidean_distance(init, right)
						right_distances.append((right_distance, right))

			try:
				left_min_distance = min(left_distances)[1]
				right_min_distance = min(right_distances)[1]
				visibility_points.append(left_min_distance)
				visibility_points.append(right_min_distance)


				left_distances = []
				right_distances = []

			except Exception as e:
				pass

		return visibility_points