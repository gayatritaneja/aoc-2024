with open('inp1.txt', 'r') as f:
	lines = f.readlines()
	l1 = []
	l2 = []
	diff = []
	for line in lines:
		line = line.split()
		l1.append(int(line[0]))
		l2.append(int(line[1]))


	l1.sort()
	l2.sort()

	for i in range(len(l1)):
		diff.append(abs(l1[i] - l2[i]))

	print(sum(diff))