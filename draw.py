import PIL
from PIL import Image, ImageDraw
import random
import math

height = 500
width = 500
sidelength = 25

def main():
	image = Image.new("RGB", (width, height), "white")
	draw = ImageDraw.Draw(image)
	removeWall(1, 1, UP)
	removeWall(2, 2, UP)
	removeWall(3, 3, UP)
	removeWall(4, 4, UP)
	removeWall(5, 5, UP)
	removeWall(6, 1, UP)
	squareRenderer.render(draw, squares)
	image.save("image.png")

def makeLikeATree(n):
	pass
	

class Square():
	def __init__(self, x, y, sidelength):
		self.x = x
		self.y = y
		self.sidelength = sidelength
		self.walls = [True, True, True, True] #Up, Right, Bottom, Left

	def removeWall(self, wallIndex):
		self.walls[wallIndex] = False

class SquareRenderer():
	def render(self, draw, squares):
		for row in squares:
			for s in row:
				if s.walls[0] : draw.line((s.x, s.y, s.x+sidelength, s.y), width=2, fill="black")
				if s.walls[1] : draw.line((s.x+sidelength, s.y, s.x+sidelength, s.y+sidelength), width=2, fill="black")
				if s.walls[2] : draw.line((s.x, s.y+sidelength, s.x+sidelength, s.y+sidelength), width=2, fill="black")
				if s.walls[3] : draw.line((s.x, s.y, s.x, s.y+sidelength), width=2, fill="black")
		
UP = ( 0, (0, -1), 2 )
RIGHT = ( 1, (1, 0), 3 )
BOTTOM = ( 2, (0, 1), 0 )
LEFT = ( 3, (-1, 0), 1 )


def removeWall(x, y, direction):
	squares[x][y].removeWall(direction[0])
	print(x, y)
	x = x + direction[1][0]
	y = y + direction[1][1]
	print(x, y)
	squares[x][y].removeWall(direction[2])


squares = [[ Square(x*sidelength,y*sidelength, sidelength) for y in range(50) ] for x in range(50) ]
squareRenderer = SquareRenderer()

main()



































