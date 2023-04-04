import pygame

class Environment():
	"""
	A class of the map where the robot will be moving around.

	Attributes
	----------
	dimensions : tuple
		The X and Y window dimensions.
	"""
	
	def __init__(self, map_dimensions):
		# Colors 
		self.WHITE = (255, 255, 255)
		self.BLACK = (0, 0, 0)
		self.RED = (255, 0, 0)
		self.GREEN = (0, 255, 0)
		self.BLUE = (0, 0, 255)
		self.BROWN = (189, 154, 122)
		self.YELLOW = (255, 255, 0)
		self.GRAY = (105, 105, 105)

		# Map dimensions
		self.WIDTH, self.HEIGHT = map_dimensions

		# Window settings
		self.FPS = 120
		pygame.display.set_caption('Visibility Polygon')
		self.map = pygame.display.set_mode(size=(self.WIDTH, self.HEIGHT))
		self.map.fill(self.WHITE)
		self.obstacles = []
		self.vertices = [(0, 0), (200, 0), (200, 70), (70, 70), (70, 200),
		 (570, 200), (570, 70), (390, 70), (390, 100), (320, 100), (320, 0),
		 (640, 0), (640, 480), (320, 480), (320, 410), (570, 410), (570, 300),
		 (70, 300), (70, 410), (150, 410), (150, 380), (220, 380), (220, 480),
		 (0, 480), (0, 0)]

	def make_map(self):
		"""
		Makes the walls of the map.
		
		Parameters
		----------
		None
		
		Returns
		-------
		list
			A collection of the vertices that compose the environment map.			
		"""
		pygame.draw.polygon(surface=self.map, color=self.GRAY, points=self.vertices)
		self.draw_walls()

		return self.vertices

	def draw_walls(self):
		"""Draws the contiguous set of lines."""
		# Draw the obstacles on top of everything
		for i in range(len(self.vertices)-1):
			pygame.draw.line(self.map, self.BLACK, self.vertices[i], self.vertices[i+1], width=4) 