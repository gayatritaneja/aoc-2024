import re

with open("inp3.txt", "r") as f:
	txt = f.read()
	l = []

	fbn = (txt.split("don't()"))
	for fb in fbn:
		fb = (fb.split("do()"))
		print(fb)
"""
		if len(fb) != 1:

				cmds = re.findall(r"mul\(\d+,\d+\)", fb[1])
				for cmd in cmds:
					nums = (cmd[4:-1]).split(",")
					nums = [int(num) for num in nums]
					l.append(nums[0] * nums[1])
		else:
				cmds = re.findall(r"mul\(\d+,\d+\)", fb[0])
				print(fb[0])
				for cmd in cmds:
					nums = (cmd[4:-1]).split(",")
					nums = [int(num) for num in nums]
					l.append(nums[0] * nums[1])


	print(sum(l))
"""
