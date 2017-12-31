import PIL
from PIL import Image, ImageDraw
import random
import math
from tree import Tree

height = 20
width = 20
sidelength = 25


def main():
	image = Image.new("RGB", (width*sidelength, height*sidelength), "white")
	draw = ImageDraw.Draw(image)
	makeMaze()
	squareRenderer.render(draw, squares)
	image.save("image.png")

def makeMaze(startX = 0, startY = 0):
	currentTile = squares[startX][startY]
	optionsExist = True
	backTrackTree = Tree( None, currentTile )
	while ( optionsExist ):
		possibleMoves = list(squareManager.getIsolatedNeighbors(currentTile.x, currentTile.y))
		if ( len(possibleMoves) > 0 ):
			move = random.choice( possibleMoves )
			currentTile = move[0]

			squareManager.removeWall(currentTile.x, currentTile.y, move[1])
			treeNode = Tree( backTrackTree, currentTile )
			backTrackTree = treeNode
			print(currentTile.x, currentTile.y)
		else: 
			if ( backTrackTree.parent != None ):
				backTrackTree = backTrackTree.parent
				currentTile = backTrackTree.value
			else:
				optionsExist = False

	

class SquareManager():
	def __init__(self, squares):
		self.squares = squares

	def getIsolatedNeighbors(self, x, y):
		neighbors = self.getNeighbors(x, y)
		return filter(lambda s: s[0].isIsolated(), neighbors)

	def getNeighbors(self, x, y):
		top = ( self.squares[x][y-1], UP) if y > 0 else None 
		right = ( self.squares[x+1][y], RIGHT) if x < width-1 else None 
		bot = ( self.squares[x][y+1], BOTTOM) if y < height-1 else None 
		left = ( self.squares[x-1][y], LEFT) if x > 0 else None 
		neighbors = [top, right, bot, left]
		return filter(lambda s: s != None, neighbors)

	def removeWall(self, x, y, direction):
		squares[x][y].removeWall(direction[0])
		x = x + direction[1][0]
		y = y + direction[1][1]
		squares[x][y].removeWall(direction[2])


class Square():
	def __init__(self, x, y, sidelength):
		self.x = x
		self.y = y
		self.walls = [True, True, True, True] #Up, Right, Bottom, Left

	def removeWall(self, wallIndex):
		self.walls[wallIndex] = False

	def isIsolated(self):
		walls = self.walls
		return walls[0] and walls[1] and walls[2] and walls[3]

class SquareRenderer():
	def render(self, draw, squares):
		w = sidelength
		for row in squares:
			for s in row:
				if s.walls[0] : draw.line((s.x*w, s.y*w, s.x*w+sidelength, s.y*w), width=2, fill="black")
				if s.walls[1] : draw.line((s.x*w+sidelength, s.y*w, s.x*w+sidelength, s.y*w+sidelength), width=2, fill="black")
				if s.walls[2] : draw.line((s.x*w, s.y*w+sidelength, s.x*w+sidelength, s.y*w+sidelength), width=2, fill="black")
				if s.walls[3] : draw.line((s.x*w, s.y*w, s.x*w, s.y*w+sidelength), width=2, fill="black")
		
UP = ( 0, (0, -1), 2 )
RIGHT = ( 1, (1, 0), 3 )
BOTTOM = ( 2, (0, 1), 0 )
LEFT = ( 3, (-1, 0), 1 )
wallDirections = (UP, RIGHT, BOTTOM, LEFT)

squares = [[ Square(x, y, sidelength) for y in range(height) ] for x in range(width) ]
squareManager = SquareManager(squares)

squareRenderer = SquareRenderer()

main()



































