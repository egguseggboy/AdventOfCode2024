class Page():
	def __init__(self, page):
		self.page = page
		self.before = []

def parseInp(lines):
	order = {}
	lists = []
	parseOrd = True

	for line in lines:
		if parseOrd:
			if line == "":
				parseOrd = False
			else:
				# Create or update a page, and list its predecessors
				# while solving, i listed and checked both predecessors/successors
				# apparently you just need one of them
				l, r = list(map(int, line.split("|")))

				if l not in order: order[l] = Page(l)
				if r not in order: order[r] = Page(r)

				order[r].before.append(l)
		else:
			lists.append(list(map(int, line.split(","))))

	return order, lists

def checkList(order, lst):
	for i in range(len(lst)):
		curr = lst[i]
		right = lst[i+1:]
		
		# Check rule violations
		for num in right:
			if num in order[curr].before:
				return 0
	
	return lst[int(len(lst) / 2)]

def correctList(order, lst):
	corrected = False

	# bubble sort lol
	for round in range(len(lst)):
		for i in range(1, len(lst)-round):
			if lst[i] in order[lst[i-1]].before:
				# swap
				lst[i-1], lst[i] = lst[i], lst[i-1]
				corrected = True
	
	# Only count corrected lists
	return lst[int(len(lst) / 2)] if corrected == True else 0

def part1(lines):
	sum = 0
	order, lists = parseInp(lines)

	for lst in lists:
		sum += checkList(order, lst)

	return sum

def part2(lines):
	sum = 0
	order, lists = parseInp(lines)

	for lst in lists:
		sum += correctList(order, lst)

	return sum

if __name__ == "__main__":
	testLines = open("test.txt").read().splitlines()
	print('[TEST]')
	print(f'Part 1: {part1(testLines)}')
	print(f'Part 2: {part2(testLines)}')

	inpLines = open("input.txt").read().splitlines()
	print('\n[INPUT]')
	print(f'Part 1: {part1(inpLines)}')
	print(f'Part 2: {part2(inpLines)}')