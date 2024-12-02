def orderCheck(arr1, rev=False):
	arr2 = sorted(arr1, reverse=rev)
	for i in range(len(arr1)):
		if arr1[i] != arr2[i]:
			return False
		
	return True

def checkArr(arr):
	diffs = []
	
	if (not(orderCheck(arr) or orderCheck(arr, rev=True))):
		return False
		
	for i in range(1, len(arr)):
		diffs.append(abs(arr[i-1] - arr[i]))

	if (max(diffs) > 3 or min(diffs) == 0):
		return False
	
	return True

def part1(lines):
	count = 0
	
	for line in lines:
		arr = list(map(int, line.split(" ")))
		
		if (checkArr(arr)):
			count += 1

	return count

def part2(lines):
	count = 0

	for line in lines:
		arr = list(map(int, line.split(" ")))
		
		if (checkArr(arr)):
			count += 1
		else:
			for i in range(len(arr)):
				if (checkArr(arr[:i] + arr[i+1:])):
					count += 1
					break

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