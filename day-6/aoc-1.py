def main():
    with open("inp6.txt", "r") as f:
        lines = f.readlines()

        unique = []
        pos = []
        
        for i in range(len(lines)):
            for j in range(len(lines[i]) - 1):
                if lines[i][j] == "^":
                    pos = [i, j]
                    unique.append(pos[:])
        
        move_up(pos, lines, unique)

        print(unique)
        print(len(unique))

def move_up(pos, lines, unique):
    while True:
        try:
            if lines[pos[0] - 1][pos[1]] != "#" and pos[0] >= 1:
                pos[0] = pos[0] - 1
                if not pos in unique:
                    unique.append(pos[:])
            elif lines[pos[0] - 1][pos[1]] == "#" and pos[0] >= 1:
                move_left(pos, lines, unique)
                break
            else:
                print(pos)
                break
        except IndexError:
            break

def move_left(pos, lines, unique):
    while True:
        try:
            if lines[pos[0]][pos[1] + 1] != "#":
                if lines[pos[0]][pos[1] + 1] != "\n":
                    pos[1] = pos[1] + 1
                else:
                    break
                if not pos in unique:
                    unique.append(pos[:])
            elif lines[pos[0]][pos[1] + 1] == "#":
                move_down(pos, lines, unique)
                break
            else:
                break
        
        except IndexError:
            break

def move_down(pos, lines, unique):
    while True:
        try:
            if lines[pos[0] + 1][pos[1]] != "#":
                pos[0] = pos[0] + 1
                if not pos in unique:
                    unique.append(pos[:])
            elif lines[pos[0] + 1][pos[1]] == "#":
                move_right(pos, lines, unique)
                break
            else:
                break
        except IndexError:
            break

def move_right(pos, lines, unique):
    while True:
        try:
            if lines[pos[0]][pos[1] - 1] != "#" and pos[1] >= 1:
                if lines[pos[0]][pos[1] - 1] != "\n":
                    pos[1] = pos[1] - 1
                else:
                    break
                if not pos in unique:
                    unique.append(pos[:])
            elif lines[pos[0]][pos[1] - 1] == "#" and pos[1] >= 1:
                move_up(pos, lines, unique)
                break
            else:
                break
        except IndexError:
            break

main()