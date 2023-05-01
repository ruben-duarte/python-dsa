# 1 x  -Push the element x into the stack.
# 2    -Delete the element present at the top of the stack.
# 3    -Print the maximum element in the stack.

# input sample
# n = 10
# 1 97
# 2
# 1 20
# 2
# 1 26
# 1 20
# 2
# 3
# 1 91
# 3
# output sample
# 26
# 91

n= 10
operations = ["1 97","2", "1 45", "1 34", "3"]

def getMax(operations):
    my_stacks = []
    for index in range(n):
        if operations[0] =="1":
            my_stacks.append(int(operations[2: ]))
        elif operations[0] == "2":
            my_stacks.pop()
        elif operations[0] == "3":
            return max(my_stacks)

getMax( ["1 97","2", "1 45", "1 34", "3"])
