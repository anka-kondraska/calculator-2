from arithmetic import *

def my_reduce(funct, lst):
    result = funct(lst[0],lst[1]) 
    short_lst = lst[2:]
    for i in range(len(short_lst)):
        result = funct(result, short_lst[i])
    print result

my_reduce(add, [10, 2, 2,2])
my_reduce(multiply, [2, 2, 2,2])
my_reduce(divide, [100, 10, 2, 2])
my_reduce(power, [2,2,2,2])