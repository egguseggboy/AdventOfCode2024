def countEmpty(list, fromInd, toNum):
	toInd = list.index(toNum)
	return toInd - fromInd

def part1(line):
	diskList = []
	currID = 0
	insID = True

	sum = 0

	# Create disk list
	for num in line:
		if insID:
			diskList += [currID] * int(num)
			currID += 1
			insID = False
		else:
			diskList += [-1] * int(num)
			insID = True

	endInd = len(diskList) - 1

	# Move each individual cell to the first empty space
	for ind in range(len(diskList) - diskList.count(-1)):
		if diskList[ind] == -1:
			sum += ind * diskList[endInd]

			while True:
				endInd -= 1
				if diskList[endInd] > -1:
					break

		else:
			sum += ind * diskList[ind]

	return sum

def part2(line):
	diskList = []
	currID = 0
	insID = True

	sizes = {}
	for i in range(10):
		sizes[i] = []

	sum = 0

	# Create disk list and sizes array
	for num in line:
		if insID:
			diskList += [currID] * int(num)
			sizes[int(num)].append(currID)

			currID += 1
			insID = False
		else:
			diskList += [-1] * int(num)
			insID = True

	for size in sizes:
		sizes[size].reverse()

	ind = 0
	num = 0
	moved = []

	while ind < len(diskList):
		# Add unmoved blocks
		while diskList[ind] != -1:
			if diskList[ind] not in moved:
				sum += ind * diskList[ind]

			num = diskList[ind]
			ind += 1

			if ind >= len(diskList):
				return sum

		# Try to fill gaps
		while diskList[ind] == -1:
			gap = countEmpty(diskList, ind, num+1)
			if gap == 0:
				ind += 1
				break

			highNum = 0
			highNumGap = 0

			# Check all blocks from size of gap to 0
			# Pick out the highest one 
			for i in range(gap, 0, -1):
				if len(sizes[i]) > 0 and sizes[i][0] > highNum:
					highNum = sizes[i][0]
					highNumGap = i

			if highNumGap > 0:
				endNum = sizes[highNumGap].pop(0)

				# Only move if block comes after current ID
				if endNum > num:
					moved.append(endNum)
					# the commented "maxNum" line added maybe an hour to my program's runtime.
					# i was trying to make an optimization with it, forgot about it, and just left it there
					# maxNum = max([n for n in diskList if n not in moved])

					for _ in range(diskList.count(endNum)):
						sum += ind * endNum
						ind += 1
			else:
				ind += 1

	return sum

if __name__ == "__main__":
	testLine = open("test.txt").read()
	print('[TEST]')
	print(f'Part 1: {part1(testLine)}')
	print(f'Part 2: {part2(testLine)}')

	inpLine = open("input.txt").read()
	print('\n[INPUT]')
	print(f'Part 1: {part1(inpLine)}')
	print(f'Part 2: {part2(inpLine)}')