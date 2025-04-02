#find max and go from there
def main():
    #with open("/Users/gayatritaneja/Documents/CS/aoc/2024/day-9/inp9.txt", "r") as f:    
        #s = f.read()
    s = "23222120202525282820202020272722212121"
    p = []
    num_digits = 0
    spaces = []

    for i in range(len(s)):
        if i % 2 == 0:
            for j in range(int(s[i])):
                p.append(str(i//2)) 
            num_digits += int(s[i])
        else:
            for j in range(int(s[i])):
                p.append(".")
                spaces.append(int(s[i]))
    
    print((p))
    
    new_p = rearrange(p)
    print((new_p))

    ans = 0
    for i in range(len(new_p)):
        if new_p[i] != ".":
            ans += (i * int(new_p[i]))
    
    print(ans)


def rearrange(p):
    new_p = p
    for i in range(int(p[-2]), -1, -1):
        if str(i) in new_p:
            num = new_p.count(str(i))
            ind = new_p.index(str(i))
            if ("." * num) in ''.join((new_p[:ind])):
                dotind = ''.join(new_p).index("." * num)
                new_p[dotind:dotind + num], new_p[ind:ind+num] = new_p[ind:ind+num], new_p[dotind:dotind + num]
            
    return new_p

if __name__ == '__main__':
    main()