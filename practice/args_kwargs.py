def function (named_arg, *args):
    print(named_arg)
    print(args)

function(1, 2, 3, 4, 5, 6, 7)

############################################3

def my_func(x, y=7, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)


my_func(1, 2, 3, 4, 5, 6, 7, a=7, b=8)

##########################################

def my_min(x, *y):
    min = x
    for i in y:
        if i < min:
            min = i
    return min

print(my_min(8, 13, 4, 42, 120, 7))

def my_minimum(s, *e):
    if s < min(e):
        return s
    else:
        return min(e)

print(my_minimum(8, 13, 4, 42, 120, 7))



###########################################

def cnuf(**kwargs):
    print(kwargs["zero"])

cnuf(a=0, zero=8)