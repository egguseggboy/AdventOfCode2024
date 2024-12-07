# Recursive approach that chops off the last number at each iteration
def rSolve(nums, target, part):
	if len(nums) == 1:
		return target == nums[0]

	# ||: Recurse if last digits of target equals last number
	if part == 2 and target % 10**len(str(nums[-1])) == nums[-1] and rSolve(nums[:-1], (target - nums[-1]) / 10**len(str(nums[-1])), part):
		return True 
	# *: Recurse if target divisible by last number
	if target % nums[-1] == 0 and rSolve(nums[:-1], target // nums[-1], part):
		return True
	# +: Recurse always
	if rSolve(nums[:-1], target - nums[-1], part):
		return True

def solve(lines, part):
	sum = 0

	for line in lines:
		nums = list(map(int, line.replace(":", "").split(" ")))
		target = nums.pop(0)

		if rSolve(nums, target, part):
			sum += target

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