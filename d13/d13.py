def solve(lines, part):
	tokens = 0

	for m in range(0, len(lines), 4):
		buttonAX, buttonAY = map(lambda x: int(x[2:]), lines[m][10:].split(", "))
		buttonBX, buttonBY = map(lambda x: int(x[2:]), lines[m+1][10:].split(", "))
		prizeX, prizeY = map(lambda x: int(x[2:]), lines[m+2][7:].split(", "))

		if part == 2:
			prizeX += 10000000000000
			prizeY += 10000000000000

		# aAX + bBX = PX, aAY + bBY = PY
		# Solve for a, b
		bNumer = buttonAX * prizeY - buttonAY * prizeX
		bDenom = buttonAX * buttonBY - buttonAY * buttonBX

		b, bRem = divmod(bNumer, bDenom)
		a, aRem = divmod(prizeY - b * buttonBY, buttonAY)

		if aRem == 0 and bRem == 0:
			if part == 2 or (a <= 100 and b <= 100):
				tokens += 3 * a + b

	return tokens

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