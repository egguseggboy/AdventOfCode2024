class Group:
	area = 0
	sides = 0

	def __init__(self, area):
		self.area = area

def ptInRange(lines, pt):
	x, y = pt
	return y in range(len(lines)) and x in range(len(lines[y]))

def addPts(pt1, pt2):
	return (pt1[0] + pt2[0], pt1[1] + pt2[1])

# Returns number of corners this cell adds
def checkCorners(lines, x, y):
	corners = 0

	flower = lines[y][x]
	# Check cells in each orthogonal direction
	N = y == 0 or lines[y-1][x] != flower
	W = x == 0 or lines[y][x-1] != flower
	S = y == len(lines)-1 or lines[y+1][x] != flower
	E = x == len(lines[y])-1 or lines[y][x+1] != flower
	# Check cells in each diagonal direction
	NW = x > 0 and y > 0 and lines[y-1][x-1] != flower
	NE = x < len(lines[y])-1 and y > 0 and lines[y-1][x+1] != flower
	SW = x > 0 and y < len(lines)-1 and lines[y+1][x-1] != flower
	SE = x < len(lines[y])-1 and y < len(lines)-1 and lines[y+1][x+1] != flower

	# Outside corner:
		# 2 cells in orthogonal directions aren't part of the group
		# This includes cells outside the map
	outCorners = sum([1 for x in [
		N and W, 
		N and E,
		S and W,
		S and E
	] if x == True])

	# Inside corner:
		# 2 cells in orthogonal directions are part of the group
		# Diagonal cell between them isn't part of group
	inCorners = sum([1 for x in [
		not (N or W) and NW,
		not (N or E) and NE,
		not (S or W) and SW,
		not (S or E) and SE,
	] if x == True])

	t = [
		not (N or W) and NW,
		not (N or E) and NE,
		not (S or W) and SW,
		not (S or E) and SE,
	]

	return outCorners + inCorners

def part1(lines):
	sum = 0
	visited = []

	for y in range(len(lines)):
		for x in range(len(lines[y])):
			if (x, y) not in visited:
				perim = 0
				area = 1
				fillQueue = [(x, y)]

				while len(fillQueue) > 0:
					flower = lines[y][x]
					currX, currY = fillQueue.pop()
					visited.append((currX, currY))

					neighbors = []
					currPerim = 4

					# Check up, down, left, right
					pts = [(currX, currY-1), (currX, currY+1), (currX-1, currY), (currX+1, currY)]

					for pt in pts:
						ptX, ptY = pt
						if ptInRange(lines, pt) and lines[ptY][ptX] == flower:
							if pt in fillQueue:
								pass
							elif pt not in visited:
								fillQueue.append(pt)
								area += 1
							else: 
								neighbors.append(pt)

					currPerim -= len(neighbors) * 2
					perim += currPerim

				sum += perim * area

	return sum


def part2(lines):
	visited = []
	cellGroups = {}
	groups = []
	currGroupNum = 0

	# Create groups
	for y in range(len(lines)):
		for x in range(len(lines[y])):
			if (x, y) not in visited:
				fillQueue = [(x, y)]
				area = 1

				while len(fillQueue) > 0:
					flower = lines[y][x]
					currX, currY = fillQueue.pop()

					visited.append((currX, currY))
					cellGroups[(currX, currY)] = currGroupNum

					# Check up, down, left, right
					pts = [(currX, currY-1), (currX, currY+1), (currX-1, currY), (currX+1, currY)]

					for pt in pts:
						ptX, ptY = pt
						if ptInRange(lines, pt) and lines[ptY][ptX] == flower:
							if pt in fillQueue:
								pass
							elif pt not in visited:
								fillQueue.append(pt)
								area += 1

				groups.append(Group(area))
				currGroupNum += 1
	
	# Check corners
	for y in range(len(lines)):
		for x in range(len(lines[y])):
			currGroup = cellGroups[(x, y)]
			# Check if cell is corner in all directions
			groups[currGroup].sides += checkCorners(lines, x, y)

	# Return sum of area * sides for all groups
	return sum([group.area * group.sides for group in groups])

if __name__ == "__main__":
	testLines = open("test.txt").read().splitlines()
	print('[TEST]')
	print(f'Part 1: {part1(testLines)}')
	print(f'Part 2: {part2(testLines)}')

	inpLines = open("input.txt").read().splitlines()
	print('\n[INPUT]')
	print(f'Part 1: {part1(inpLines)}')
	print(f'Part 2: {part2(inpLines)}')