import os

def sum_of_squares(values, ls=[]):
    for value in values:
        ls.append(value ** 2)
    return sum(ls)

os.environ["PYTHONBREAKPOINT"] = "mypdb.set_trace"
breakpoint()
print("here")
print(1, 2, 3, sum_of_squares([1, 2, 3]))
print(3, 2, 1, sum_of_squares([3, 2, 1]))

# the initialized array ls still stores the previous sum from before
