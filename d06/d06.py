def findGuard(lines):
	for i in range(len(lines)):
		line = lines[i]

		if "^" in line:
			return (line.index("^"), i)

def addPoints(pt1, pt2):
	return (pt1[0] + pt2[0], pt1[1] + pt2[1])

def getCell(lines, point):
	return lines[point[1]][point[0]]

def posOnEdge(lines, point):
	return point[0] in [0, len(lines[0])-1] or point[1] in [0, len(lines)-1]

def part1(lines):
	currPos = findGuard(lines)
	currDir = 0
	dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

	visited = set()

	while (not posOnEdge(lines, currPos)):
		visited.add(currPos)
		nextPos = addPoints(currPos, dirs[currDir])

		if getCell(lines, nextPos) == "#":
			currDir += 1; currDir %= 4
			nextPos = addPoints(currPos, dirs[currDir])

		currPos = nextPos

	return len(visited) + 1

# i have no idea how to make this faster sorry
def part2(lines):
	startPos = findGuard(lines)
	startDir = 0

	currPos = startPos
	currDir = startDir
	dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

	count = 0

	# Get a list of all cells visited in the original pass
	origVisited = set()

	while (not posOnEdge(lines, currPos)):
		origVisited.add(currPos)
		nextPos = addPoints(currPos, dirs[currDir % 4])

		while getCell(lines, nextPos) == "#":
			currDir += 1
			nextPos = addPoints(currPos, dirs[currDir % 4])

		currPos = nextPos

	origVisited.add(currPos)
	
	for y in range(len(lines)):
		for x in range(len(lines[0])):
			currBlock = (x, y)

			# Only run through if:
				# current block was visited in original pass
				# current block is not start position or a #
			if currBlock not in origVisited or currBlock == startPos or getCell(lines, currBlock) == "#":
				continue

			currPos = startPos; currDir = startDir
			visited = set()

			while (not posOnEdge(lines, currPos)):
				if (currPos, currDir) in visited:
					count += 1
					break

				visited.add((currPos, currDir))
				nextPos = addPoints(currPos, dirs[currDir])

				while getCell(lines, nextPos) == "#" or nextPos == currBlock:
					currDir += 1; currDir %= 4
					nextPos = addPoints(currPos, dirs[currDir])

				currPos = nextPos

	return count

if __name__ == "__main__":
	testLines = open("test.txt").read().splitlines()
	print('[TEST]')
	print(f'Part 1: {part1(testLines)}')
	print(f'Part 2: {part2(testLines)}')

	inpLines = open("input.txt").read().splitlines()
	print('\n[INPUT]')
	print(f'Part 1: {part1(inpLines)}')
	print(f'Part 2: {part2(inpLines)}')