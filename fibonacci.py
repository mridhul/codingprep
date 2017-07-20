mem = {}

# def fib(n):
#     if n<2:
#         return (n)
#     elif n not in mem.keys():
#         mem[n] = fib(n -1 ) + fib(n -2)
#     return mem[n]
#
# print fib(39)

def fib(n):
    if n<2:
        return (n)
    else:
        return fib(n-1)+fib(n-2)

print fib(332)