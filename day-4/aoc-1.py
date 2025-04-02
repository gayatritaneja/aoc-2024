def main():
	with open("inp.txt", "r") as f:
		text = f.readlines()
		count = 0

		for i in range(len(text)):
			for j in range(140):
				if text[i][j] == "X":
					if search_fwd(i, j, text):
						count += 1
					if search_bwd(i, j, text):
						count += 1
					if search_dwn(i, j, text):
						count += 1
					if search_up(i, j, text):
						count += 1
					if search_dup1(i, j, text):
						count += 1
					if search_dup2(i, j, text):
						count += 1
					if search_ddwn1(i, j, text):
						count += 1
					if search_ddwn2(i, j, text):
						count += 1

		print(count)


def search_fwd(i, j, text):
	
	try:

		if text[i][j+1] == "M" and text[i][j+2] == "A" and text[i][j+3] == "S":
			return True
		else:
			return False
	except IndexError:
		return False

def search_bwd(i, j, text):

	try:

		if text[i][j-1] == "M" and text[i][j-2] == "A" and text[i][j-3] == "S" and (j >= 3):
			return True
		else:
			return False
	except IndexError:
		return False

def search_dwn(i, j, text):

	try:
		if text[i+1][j] == "M" and text[i+2][j] == "A" and text[i+3][j] == "S":
			return True
		else:
			return False
	except IndexError:
		return False

def search_up(i, j, text):

	try:
		if text[i-1][j] == "M" and text[i-2][j] == "A" and text[i-3][j] == "S" and (i >= 3):
			return True
		else:
			return False
	except IndexError:
		return False

def search_ddwn1(i, j, text):

	try:
		if text[i+1][j-1] == "M" and text[i+2][j-2] == "A" and text[i+3][j-3] == "S" and (j >= 3):
			return True
		else:
			return False
	except IndexError:
		return False

def search_ddwn2(i, j, text):

	try:
		if text[i+1][j+1] == "M" and text[i+2][j+2] == "A" and text[i+3][j+3] == "S":
			return True
		else:
			return False
	except IndexError:
		return False

def search_dup1(i, j, text):

	try:
		if text[i-1][j-1] == "M" and text[i-2][j-2] == "A" and text[i-3][j-3] == "S" and (i >= 3 and j >= 3):
			return True
		else:
			return False
	except IndexError:
		return False

def search_dup2(i, j, text):

	try:
		if text[i-1][j+1] == "M" and text[i-2][j+2] == "A" and text[i-3][j+3] == "S" and (i >= 3):
			return True
		else:
			return False
	except IndexError:
		return False


main()