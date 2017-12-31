from PIL import Image, ImageDraw
import random

# Height and Width in number of squares.
height = 20
width = 20
sidelength = 25

# Adding 2 pixels to image size to allow for the outermost walls to be drawn
pixelHeight = height*sidelength+2
pixelWidth = width*sidelength+2


def main():
	image = Image.new("RGB", (pixelWidth, pixelHeight), "white")
	draw = ImageDraw.Draw(image)
	makeMaze()
	squareRenderer.render(draw, squares)
	image.save("image.png")


def makeMaze(startX = 0, startY = 0):
	""" Generates a maze by standard backtracking algorithm
		Begins at the given start coordinates, taking a random direction
		Candidates for random directions are exclusively isolated neighbors
		Then iterates, backtracking if no neighbors are isolated
		and terminating, when backtracking leads to the starting node """
	currentTile = squares[startX][startY]
	moveOptionsExist = True
	backtrackTree = ParentPointerTree( None, currentTile )
	while ( moveOptionsExist ):
		possibleMoves = squareManager.getIsolatedNeighbors( currentTile )
		if ( len( possibleMoves ) > 0 ):
			move = random.choice( possibleMoves )
			squareManager.removeWall( currentTile, move[1] )
			currentTile = move[0]
			backtrackTree = ParentPointerTree( backtrackTree, currentTile )
		else: 
			if ( backtrackTree.parent != None ):
				backtrackTree = backtrackTree.parent
				currentTile = backtrackTree.value
			else:
				moveOptionsExist = False

class ParentPointerTree():
	""" No need to implement a full tree, since we only need backtracking """
	def __init__(self, parent, value):
		self.parent = parent
		self.value = value

class SquareManager():
	def __init__(self, squares):
		self.squares = squares

	def getIsolatedNeighbors(self, square):
		neighbors = self.getNeighbors(square)
		return list( filter( lambda s: s[0].isIsolated(), neighbors ) )

	def getNeighbors(self, square):
		""" Return all neighbors combined with the direction they're in. """
		x = square.x
		y = square.y
		# Ternary assignment required to properly handle squares along the edges
		top = ( self.squares[x][y-1], UP) if y > 0 else None 
		right = ( self.squares[x+1][y], RIGHT) if x < width-1 else None 
		bot = ( self.squares[x][y+1], BOTTOM) if y < height-1 else None 
		left = ( self.squares[x-1][y], LEFT) if x > 0 else None 
		neighbors = [top, right, bot, left]
		return list( filter( lambda s: s != None, neighbors ) )

	def removeWall(self, square, direction):
		""" In removing a wall, the neighbors wall in that direction also has to be deactivated, since each line is drawn twice """
		x = square.x
		y = square.y
		squares[x][y].removeWall(direction[0])
		x = x + direction[1][0]
		y = y + direction[1][1]
		squares[x][y].removeWall(direction[2])


class Square():
	def __init__(self, x, y, sidelength):
		self.x = x
		self.y = y
		self.walls = [True, True, True, True] #Up, Right, Bottom, Left, as used in CSS

	def removeWall(self, wallIndex):
		self.walls[wallIndex] = False

	def isIsolated(self):
		""" A square is defined to be isolated if all it's walls are intact """
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
		
""" These four directions consist of:
	The wall index to be removed from current square
	A tuple giving (x, y)-directions for getting to the related square
	The wall index to be removed from the related square """
UP = ( 0, (0, -1), 2 )
RIGHT = ( 1, (1, 0), 3 )
BOTTOM = ( 2, (0, 1), 0 )
LEFT = ( 3, (-1, 0), 1 )

squares = [ [ Square(x, y, sidelength) for y in range(height) ] for x in range(width) ]
squareManager = SquareManager(squares)
squareRenderer = SquareRenderer()

main()