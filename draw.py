import PIL
from PIL import Image, ImageDraw
import random

height = 500
width = 500
sidelength = 25

def main():
	image = Image.new("RGB", (width, height), "white")
	draw = ImageDraw.Draw(image)

	squareRenderer.render(draw, squares)
	image.save("image.png")

def makeLikeATree(n):
	pass


class Square():
	def __init__(self, x, y, sidelength):
		self.x = x
		self.y = y
		self.sidelength = sidelength
		self.walls = (True, False, True, True) #Up, Right, Bottom, Left

class SquareRenderer():
	def render(self, draw, squares):
		for s in squares:
			if s.walls[0] : draw.line((s.x, s.y, s.x+sidelength, s.y), width=2, fill="black")
			if s.walls[1] : draw.line((s.x, s.y, s.x, s.y+sidelength), width=2, fill="black")
			if s.walls[2] : draw.line((s.x+sidelength, s.y, s.x+sidelength, s.y+sidelength), width=2, fill="black")
			if s.walls[3] : draw.line((s.x, s.y+sidelength, s.x+sidelength, s.y+sidelength), width=2, fill="black")
		


squares = [Square(x*sidelength,y*sidelength, sidelength) for x in range(50) for y in range(50)]
squareRenderer = SquareRenderer()

main()