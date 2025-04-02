with open("inp2.txt", "r") as f:
	lines = f.readlines()

	safe = []

	for line in lines:
		line  = [int(elem)  for elem in line.split()]

		if line[0] < line[1]:

			for i in range(len(line) - 1):	
				if line[i] < line[i+1] and ((i + 1) != len(line)):
					continue
				else:
					break

			else:
				t = []
				for i in range(len(line) - 1):
					t.append(abs(line[i] - line[i + 1]))

				for elem in t:
					if elem > 3:
						break
				else:
					safe.append(line)

		if line[0] > line[1]:

			for i in range(len(line) - 1):	
				if line[i] > line[i+1] and ((i + 1) != len(line)):
					continue
				else:
					break

			else:
				t = []
				for i in range(len(line) - 1):
					t.append(abs(line[i] - line[i + 1]))

				for elem in t:
					if elem > 3:
						break
				else:
					safe.append(line)

	print(safe)
	print(len(safe))

