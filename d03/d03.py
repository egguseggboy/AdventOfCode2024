import re

def part1(lines):
	sum = 0

	for line in lines:
		muls = re.findall("mul\(\d+\,\d+\)", line)

		for mul in muls:
			strNums = mul[mul.index("(")+1 : -1]
			
			nums = list(map(int, strNums.split(",")))
			
			sum += nums[0] * nums[1]

	return sum

def part2(lines):
	sum = 0
	calc = True

	for line in lines:
		ops = re.findall("(mul\(\d+\,\d+\)|do\(\)|don't\(\))", line)

		for op in ops:
			if (op == "don't()"):
				calc = False
			elif (op == "do()"):
				calc = True
			elif (calc == True):
				strNums = op[op.index("(")+1 : -1]
				
				nums = list(map(int, strNums.split(",")))
				
				sum += nums[0] * nums[1]

	return sum

if __name__ == "__main__":
	testLines = open("test.txt").readlines()
	print('[TEST]')
	print(f'Part 1: {part1(testLines)}')
	print(f'Part 2: {part2(testLines)}')

	inpLines = open("input.txt").read().splitlines()
	print('\n[INPUT]')
	print(f'Part 1: {part1(inpLines)}')
	print(f'Part 2: {part2(inpLines)}')