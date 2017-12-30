
#merely a sketch of a test
def GetNeighborsTest():
	for x, y in ((0, 2), (5, 0), (19, 3), (6, 19), (0, 0)):
	for s in squareManager.getNeighbors(x, y):
		print(s.x, s.y)
	print("\n")