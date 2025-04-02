import re

with open("inp3.txt", "r") as f:
	txt = f.read()
	cmds = re.findall(r"mul\(\d+,\d+\)", txt)
	l = []

	for cmd in cmds:
		nums = (cmd[4:-1]).split(",")
		nums = [int(num) for num in nums]
		l.append(nums[0] * nums[1])

	print(sum(l))