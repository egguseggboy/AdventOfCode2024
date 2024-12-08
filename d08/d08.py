def addPts(pt1, pt2):
	return (pt1[0] + pt2[0], pt1[1] + pt2[1])

def negPt(pt):
	return(-pt[0], -pt[1])

def getDist(pt1, pt2):
	return addPts(pt1, negPt(pt2))

def ptInBounds(pt, maxX, maxY):
	return pt[0] >= 0 and pt[0] < maxX and pt[1] >= 0 and pt[1] < maxY

def solve(lines, part):
	antennas = dict()
	antinodes = set()

	# Get list of antennas, storing them by frequency
	for y in range(len(lines)):
		for x in range(len(lines[0])):
			cell = lines[y][x]
			if cell != ".":
				if cell not in antennas:
					antennas[cell] = [(x, y)]
				else:
					antennas[cell].append((x, y))

	# Create antinodes for every pair of antennas
	for ant in antennas:
		arr = antennas[ant]
		for i in range(len(arr)-1):
			currPt = arr[i]; otherPts = arr[i+1:]
			for otherPt in otherPts:
				step = getDist(currPt, otherPt)
				dist = step
				offCurrToAdd = True; offOtherToAdd = True

				if part == 2:
					antinodes.add(currPt)
					antinodes.add(otherPt)
				
				# While points to add in line, keep adding
				# (only add 1 in each direction for part 1)
				while offCurrToAdd or offOtherToAdd:
					offCurr = addPts(currPt, dist)
					
					offOther = addPts(otherPt, negPt(dist))

					# Add in direction of current point
					if (offCurrToAdd and ptInBounds(offCurr, len(lines[0]), len(lines))):
						antinodes.add(offCurr)
					else:
						offCurrToAdd = False

					# Add in direction of other point
					if (offOtherToAdd and ptInBounds(offOther, len(lines[0]), len(lines))):
						antinodes.add(offOther)
					else:
						offOtherToAdd = False

					dist = addPts(dist, step)

					# Only add 1 point in each direction for part 1
					if part == 1:
						break

	return len(antinodes)

def part1(lines):
	return solve(lines, 1)

def part2(lines):
	return solve(lines, 2)

if __name__ == "__main__":
	testLines = open("test.txt").read().splitlines()
	print('[TEST]')
	print(f'Part 1: {part1(testLines)}')
	print(f'Part 2: {part2(testLines)}')

	inpLines = open("input.txt").read().splitlines()
	print('\n[INPUT]')
	print(f'Part 1: {part1(inpLines)}')
	print(f'Part 2: {part2(inpLines)}')