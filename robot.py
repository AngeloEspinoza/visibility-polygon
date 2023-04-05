import pygame
import math

class Robot():
	"""
	A class for the holonomic robot.

	Attributes
	----------
	start : tuple
		Initial position of the tree in X and Y respectively.
	radius : int
		End position of the tree in X and Y respectively.
	vertices : list
		List of the vertices of the map.
	"""
	def __init__(self, start, radius, vertices):
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
		self.start = start
		self.radius = radius
		self.vertices = vertices
		self.end_points = []
		self.visibility_points = []

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

	def get_ray_angle(self, p1, p2):
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

	def intersect(self, obstacles, point1, point2):
		"""Checks the intersection of two lines.

		Given a set of lines, and the initial and end point of a line, it 
		computes the intersection between the line and the set of lines.

		Parameters
		----------
		obstacles : list
			List of lines to be checked for intersection.
		point1 : tuple
			Coordinate of the start of the line.
		point2 : tuple
			Coordinate of the end of the line.

		Returns
		-------
		tuple
			Coordinate where the line intersects.
		"""
		best_distance = math.inf
		end_point = point2

		for point3, point4 in obstacles:
			# Compute distance from a point to a line
			distance = (point2[0]-point1[0]) * (point4[1]-point3[1]) + \
				(point2[1]-point1[1]) * (point3[0]-point4[0]) 

			if distance != 0:
				t = ((point3[0]-point1[0]) * (point4[1]-point3[1]) + \
					(point3[1]-point1[1]) * (point3[0]-point4[0])) / distance
				u = ((point3[0]-point1[0]) * (point2[1]-point1[1]) + \
					(point3[1]-point1[1]) * (point1[0]-point2[0])) / distance
	            
				if 0 <= t <= 1 and 0 <= u <= 1:
					vx, vy = (point2[0]-point1[0]) * t, \
						(point2[1]-point1[1]) * t
					dist = vx*vx + vy*vy

					if dist < best_distance:
						px, py = round(point4[0] * u + point3[0] * (1-u)), \
							round(point4[1] * u + point3[1] * (1-u))
						best_distance = dist
						end_point = (px, py)

		return end_point

	def get_offset_end_points(self, init):
		"""Initializes the rays by getting the two angle offsets.

		Given the robot's position, it will cast rays with an angle and distance
		offset.
		
		Parameters
		----------
		init : tuple
			Coordinate of the robot's position from where the rays will
			be casted from.

		Returns
		-------
		None
		"""
		offset = 0.013
		ray_length = 1000

		for vertice in self.vertices:
			angle = self.get_ray_angle(init, vertice)
			angle_left = angle - offset
			angle_left %= math.pi * 2
			angle_right = angle + offset
			angle_right %= math.pi * 2

			dst = self.euclidean_distance(init, vertice)
			left_offset = tuple([init[0] + (ray_length + dst) * math.cos(angle_left), init[1] +
				(ray_length + dst) * math.sin(angle_left)])
			right_offset = tuple([init[0] + (ray_length + dst) * math.cos(angle_right), init[1] +
				(ray_length + dst) * math.sin(angle_right)])

			self.end_points.append(left_offset)
			self.end_points.append(right_offset)
			self.end_points.append(vertice)

	def generate_visibility_points(self):
		"""Initializes the rays by applying an algorithm."""

		# List of lines that represent the boundaries of the environment
		obstacles = [(self.vertices[i], self.vertices[i+1]) for i in range(len(self.vertices)-1)]

		for point in self.end_points:
			intersection_point = self.intersect(obstacles=obstacles, point1=self.start,
				point2=point)
			self.visibility_points.append(intersection_point)

	def cast_rays(self, init):
		"""Gets the rays initiliazed."""
		self.get_offset_end_points(init=init)
		self.generate_visibility_points()

	def draw(self, map):
		"""Draws the robot on map."""
		pygame.draw.circle(surface=map, color=self.BLACK, center=self.start, radius=self.radius)

	def draw_cloud_points(self, map):
		"""Draws the cloud points reflected in the walls of the obstacles."""
		for point in self.visibility_points:
			pygame.draw.circle(map, self.RED, point, 3)

	def draw_rays(self, map):
		"""Draws a raytracing from the robot's position."""
		for point in self.visibility_points:
			pygame.draw.line(map, self.RED, self.start, point)
	
	def draw_visibility_polygon(self, map):
		"""Draws the visibility polygon given a set of points."""
		ordered_points = []
		for point in self.visibility_points:
			angle = self.get_ray_angle(self.start, point)
			ordered_points.append((angle, point))
		
		ordered_points.sort()
		ordered_points = [point[1] for point in ordered_points]
		pygame.draw.polygon(surface=map, color=self.YELLOW, points=ordered_points)
		self.draw(map=map)
		self.visibility_points = []
		self.end_points = []