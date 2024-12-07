import numpy as np

def useOp(num1, num2, op):
	match op:
		case "+":
			return num1 + num2
		case "*":
			return num1 * num2
		case "||":
			return (num1 * 10**len(str(num2))) + num2

def buildAndSolveEq(nums, comboNum, base, target):
	ops = ['+', '*', '||']
	comboDigits = np.base_repr(comboNum, base).zfill(len(nums)-1)
	
	opCombo = [ops[int(digit)] for digit in list(str(comboDigits))]

	result = nums[0]
	for i in range(1, len(nums)):
		result = useOp(result, nums[i], opCombo[i-1])

		if (result > target):
			return 0

	return result

def solve(lines, base):
	sum = 0

	for line in lines:
		nums = list(map(int, line.replace(":", "").split(" ")))
		target = nums.pop(0)

		for i in range(base**(len(nums)-1)):
			if target == buildAndSolveEq(nums, i, base, target):
				sum += target
				break

	return sum

def part1(lines):
	return solve(lines, 2)

def part2(lines):
	return solve(lines, 3)

if __name__ == "__main__":
	testLines = open("test.txt").read().splitlines()
	print('[TEST]')
	print(f'Part 1: {part1(testLines)}')
	print(f'Part 2: {part2(testLines)}')

	inpLines = open("input.txt").read().splitlines()
	print('\n[INPUT]')
	print(f'Part 1: {part1(inpLines)}')
	print(f'Part 2: {part2(inpLines)}')