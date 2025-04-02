def main():
    with open("inp9.txt", "r") as f:    
        s = f.read()
    

    p = []
    num_digits = 0

    for i in range(len(s)):
        if i % 2 == 0:
            for j in range(int(s[i])):
                p.append(str(i//2)) 
            num_digits += int(s[i])
        else:
            for j in range(int(s[i])):
                p.append(".")
    

    new_p = rearrange(p, num_digits)


    ans = 0
    for i in range(num_digits):
        ans += (i * int(new_p[i]))
    
    print(ans)


def rearrange(p, num_digits):

    i = 1
    p_list = p

    while cont_string(p_list, num_digits):
            
        ind = p_list.index(".")
        p_list[-i], p_list[ind] = p_list[ind], p_list[-i]

        i += 1

    return p_list

def cont_string(p, num_digits):
    p_check = p[:num_digits]
    for i in range(len(p_check)):
        if p_check[i].isdigit():
            continue
        else:
            return True
    return False


if __name__ == '__main__':
    main()