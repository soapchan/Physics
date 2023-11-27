import pygame


pygame.init()


class Screen:
	def __init__(self):
		self.width = 500
		self.height = 500
		self.colour = 255, 255, 255
		self.screen = pygame.display.set_mode((self.width, self.height))


screen = Screen()


class Cube:
	def __init__(self, x, y, width, height, xvel, yvel, colour, grounded, gravity):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.xvel = xvel
		self.yvel = yvel
		self.colour = colour
		self.grounded = grounded
		self.rect = pygame.Rect(x, y, self.width, self.height)
		self.gravity = gravity


	def redefine(self):
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


	def draw(self):
		pygame.draw.rect(screen.screen, self.colour, self.rect)
		self.redefine()


	def fall(self):
		...


red_cube = Cube(x=100, y=250, width=50, height=50, xvel=0, yvel=0, colour=(255, 0, 0), grounded=False, gravity=0.5)
blue_cube = Cube(x=300, y=250, width=50, height=50, xvel=0, yvel=0, colour=(0, 0, 255), grounded=False, gravity=0.5)
floor = Cube(x=0, y=450, width=500, height=50, xvel=0, yvel=0, colour=(0, 255, 0), grounded=True, gravity=0)


running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.screen.fill(screen.colour)
	red_cube.draw()
	blue_cube.draw()
	blue_cube.fall()
	floor.draw()
	pygame.display.flip()
