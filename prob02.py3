
inp = input()
nums = [int(x) for x in inp.split()]
if nums[1] / nums[0] <= nums[2]:
    print(inp + '. I will make it!')
else:
    print(inp + '. I will be late!')