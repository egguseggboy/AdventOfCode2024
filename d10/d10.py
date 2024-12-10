# Check every direction where tile ascends by 1, ends when 9 is reached
# Part 1 returns a list of all peaks reached for a trail
# Part 2 returns number of ways to reach every trail
def recurse(lines, x, y, val, part):
	result = list() if part == 1 else 0
	if val == 9 and lines[y][x] == "9":
		return [(x, y)] if part == 1 else 1

	# -x
	if x-1 >= 0 and lines[y][x-1] == str(val+1):
		result += recurse(lines, x-1, y, val+1, part)
	# +x
	if x+1 < len(lines[0]) and lines[y][x+1] == str(val+1):
		result += recurse(lines, x+1, y, val+1, part)
	# -y
	if y-1 >= 0 and lines[y-1][x] == str(val+1):
		result += recurse(lines, x, y-1, val+1, part)
	# +y
	if y+1 < len(lines) and lines[y+1][x] == str(val+1):
		result += recurse(lines, x, y+1, val+1, part)

	return result

def solve(lines, part):
	sum = 0
	for y in range(len(lines)):
		for x in range(len(lines[0])):
			if lines[y][x] == "0":
				res = recurse(lines, x, y, 0, part)
				sum += len(set(res)) if part == 1 else res

	return sum

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