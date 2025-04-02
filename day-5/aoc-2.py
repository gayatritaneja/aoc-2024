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
            if not check_valid(order, seq):
                newseq = rearrange(order, seq)
                valid_mid.append(newseq[int((len(newseq)-1)/2)])

        
        print(sum(valid_mid))
    
def check_valid(order, l):

    for i in range(len(l) - 1):
        str = f"{l[i]}|{l[i+1]}\n"
        if str in order:
            continue
        else:
            return False
    return True

def rearrange(order, l):
    n = 1

    for j in range(len(l)-1):
        for i in range(len(l) - n):
            str = f"{l[i]}|{l[i+1]}\n"
            if str in order:
                continue
            else:
                l[i], l[i+1] = l[i+1], l[i]
        n += 1
    print(l)        
    return l


main()