def part1(lines):
	sum = 0
	LList = []; RList = []

	for line in lines:
		l, r = map(int, line.split("   "))
		LList.append(l)
		RList.append(r)

	LList.sort()
	RList.sort()

	for i in range(len(LList)):
		sum += abs(LList[i] - RList[i])

	return sum

def part2(lines):
	sum = 0
	counts = {}
	LList = [];	RList = []

	for line in lines:
		l, r = map(int, line.split("   "))

		if r in counts:
			counts[r] += 1
		else:
			counts[r] = 1

		LList.append(l)
		RList.append(r)

	for elem in LList:
		if elem in RList:
			sum += int(elem) * counts[elem]

	return sum

if __name__ == "__main__":
	lines = open("input.txt").read().splitlines()
	
	print(f'Part 1: {part1(lines)}')
	print(f'Part 2: {part2(lines)}')