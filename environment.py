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
		

	def make_map(self):
		"""
		Makes the halls of the map.
		
		Parameters
		----------
		None
		
		Returns
		-------
		list
			A collection of the vertices that compose the environment map.			
		"""
		x, y = 0, 0
		width, height = 50, 200
		points = [(0, 0), (200, 0), (200, 70), (70, 70), (70, 200), (570, 200),
		 (570, 70), (390, 70), (390, 100), (320, 100), (320, 0), (640, 0),
		 (640, 480), (320, 480), (320, 410), (570, 410), (570, 300), (70, 300),
		 (70, 410), (150, 410), (150, 380), (220, 380), (220, 480), (0, 480), (0, 0)];

		pygame.draw.polygon(surface=self.map, color=self.GRAY,
			points=points)


		# print(xd.collidepoint((10,10)))

		pygame.draw.line(surface=self.map, color=self.RED, 
				start_pos=(0, 0), end_pos=(200, 0), width=3)

		for i in range(len(points)-1):
			pygame.draw.line(surface=self.map, color=self.GRAY, 
				start_pos=points[i], end_pos=points[i+1], width=3)

		rects = [pygame.draw.rect(self.map, self.BLACK, pygame.Rect(0, 0, 200, 1)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(200, 0, 3, 70)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(70, 67, 130, 3)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(70, 70, 3, 130)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(70, 197, 500, 3)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(567, 70, 3, 130)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(393, 70, 170, 3)),
		# pygame.draw.rect(self.map, self.BLACK, pygame.Rect(390, 67, 180, 3)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(390, 70, 3, 30)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(320, 100, 72, 3)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(320, 0, 3, 100)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(320, 0, 320, 3)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(640, 0, 3, 480)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(320, 477, 640, 3)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(320, 410, 3, 70)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(320, 410, 250, 3)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(567, 300, 3, 113)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(70, 300, 503, 3)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(70, 300, 3, 110)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(70, 410, 80, 3)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(150, 380, 3, 33)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(150, 380, 70, 3)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(220, 380, 3, 100)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(0, 477, 220, 3)),
		pygame.draw.rect(self.map, self.BLACK, pygame.Rect(0, 0, 3, 480))]


		# print(environment.collidepoint((100, 100)))

		return points, rects