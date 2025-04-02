def main():
    with open("inp5.txt", "r") as f:
        lines = f.readlines()

        order = []
        tbe = []
        valid_mid = []
        
        for line in lines:
            if "|" in line:
                order.append(line)
            else:
                if line != "\n":
                    line = line.split(",")
                    line = [int(elem) for elem in line]
                    tbe.append(line)
        
        for seq in tbe:
            if check_valid(order, seq):
                print(seq)
                valid_mid.append(seq[int((len(seq)-1)/2)])
        
        print(sum(valid_mid))

    
def check_valid(order, l):

    for i in range(len(l) - 1):
        str = f"{l[i]}|{l[i+1]}\n"
        if str in order:
            continue
        else:
            return False
    return True


main()