def searchDir(lines, x, y, xD, yD):
	xLen = len(lines)
	yLen = len(lines[0])

	if (x + 3 * xD not in range(0, xLen)) or (y + 3 * yD not in range(0, yLen)):
		return 0
	
	result = "".join(lines[y + i * yD][x + i * xD] for i in range(4))

	return 1 if result == "XMAS" else 0


def part1(lines):
	count = 0
	xLen = len(lines)
	yLen = len(lines[0])

	# At every point, searches for "XMAS" in every compass direction
	for y in range(yLen):
		for x in range(xLen):
			count += searchDir(lines, x, y, 1, 1)	# SE
			count += searchDir(lines, x, y, 1, 0)	# E
			count += searchDir(lines, x, y, 1, -1)	# NE

			count += searchDir(lines, x, y, 0, 1)	# S
			count += searchDir(lines, x, y, 0, -1)	# N

			count += searchDir(lines, x, y, -1, 1)	# SW
			count += searchDir(lines, x, y, -1, 0)	# W
			count += searchDir(lines, x, y, -1, -1)	# NW

	return count

def part2(lines):
	count = 0
	xLen = len(lines)
	yLen = len(lines[0])

	for y in range(yLen - 2):
		for x in range(xLen - 2):
			# Get corners and middle of 3x3 range
			NW = lines[y][x]
			NE = lines[y][x+2]
			C  = lines[y+1][x+1]
			SW = lines[y+2][x]
			SE = lines[y+2][x+2]

			chars = NW + NE + SW + SE

			if C == "A" and chars.count("M") == 2 and chars.count("S") == 2:
				if (NW + NE == SW + SE) or (NW + SW == NE + SE):
					count += 1

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