import itertools

def main():
    with open("inp7.txt", "r") as f:
        lines = f.readlines()
        final_ans = 0
        for line in lines:
            ans, nums = line.split(": ")
            nums = [int(num) for num in str(nums).split(" ")]
            ans = int(ans)

            if check_all_operations(nums, ans):
                final_ans += ans
        
        print(final_ans)

def check_all_operations(nums, ans):
    ops_list = list(itertools.product(['+', '*', "||"], repeat = len(nums) - 1))
    
    for j in range(len(ops_list)):

        if evaluate(nums, ops_list[j]) != ans:
            continue

        else:
            return True
    
    return False


def evaluate(nums, ops):
    ans = nums[0]
    for i in range(len(nums) - 1):
        if ops[i] == "+":
            ans += (nums[i + 1])
        elif ops[i] == "*":
            ans *= nums[i + 1]
        elif ops[i] == "||":
            ans = str(ans)
            ans = ans + str(nums[i + 1])
            ans = int(ans)
    
    return ans

main()