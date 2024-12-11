import functools

# Tried adding pre-baked results for some common numbers (0, 1, 2, 4, 2024, etc) but it made no difference in performance
@functools.lru_cache(None)
def recurse(rock, depth, maxDepth):
	if depth == maxDepth:
		return 1
	
	result = 0

	if rock == 0:
		if depth == maxDepth-1:
			result += 1
		else:
			result += recurse(2024, depth+2, maxDepth)
	elif len(str(rock)) % 2 == 0:
		strRock = str(rock)
		mid = len(strRock) // 2
		result += recurse(int(strRock[:mid]), depth+1, maxDepth)
		result += recurse(int(strRock[mid:]), depth+1, maxDepth)
	else:
		result += recurse(rock*2024, depth+1, maxDepth)
	
	return result

def solve(line, maxDepth):
	rocks = list(map(int, line.split(" ")))

	return sum((recurse(rock, 0, maxDepth)) for rock in rocks)

def part1(line):
	return solve(line, 25)

def part2(line):
	return solve(line, 75)

if __name__ == "__main__":
	testLine = open("test.txt").read()
	print('[TEST]')
	print(f'Part 1: {part1(testLine)}')
	print(f'Part 2: {part2(testLine)}')

	inpLine = open("input.txt").read()
	print('\n[INPUT]')
	print(f'Part 1: {part1(inpLine)}')
	print(f'Part 2: {part2(inpLine)}')