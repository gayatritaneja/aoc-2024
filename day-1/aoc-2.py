with open('inp1.txt', 'r') as f:
	lines = f.readlines()
	l1 = []
	l2 = []

	for line in lines:
		line = line.split()
		l1.append(int(line[0]))
		l2.append(int(line[1]))

	sim = 0

	for i in range(len(l1)):
		ad = l2.count(l1[i]) * l1[i]
		sim += ad

	print(sim)