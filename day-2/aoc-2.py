def main():
	with open("inp2.txt", "r") as f:
		lines = f.readlines()

		safe = []
		unsafe = []

		for line in lines:
			line  = [int(elem)  for elem in line.split()]

			if safety(line):
				safe.append(line)
			else:
				unsafe.append(line)

		for li in unsafe:
			
			for i in range(0, len(li)):
				newline = li[:]
				newline.pop(i)
				if not safety(newline):
					newline = li
					continue
				else:
					safe.append(newline)
					break

		print(len(safe))


def safety(line):


	if line[0] < line[1]:

		for i in range(len(line) - 1):	
			if line[i] < line[i+1]:
				continue
			else:
				return False

		else:
			t = []
			for i in range(len(line) - 1):
				t.append(abs(line[i] - line[i + 1]))

			for elem in t:
				if elem > 3:
					return False
			else:
				return True

	if line[0] > line[1]:

		for i in range(len(line) - 1):	
			if line[i] > line[i+1]:
				continue
			else:
				return False

		else:
			t = []
			for i in range(len(line) - 1):
				t.append(abs(line[i] - line[i + 1]))

			for elem in t:
				if elem > 3:
					return False
			else:
				return True


main()
