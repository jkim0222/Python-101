# Fibonacci numbers 3 ways
# 5/23/17 Jeju National University
# Jungju Kim

from datetime import datetime

def iterative_fib(n):
    if n <=2:
        return 1
    else:
        f_2 = 1
        f_1 = 1
        for i in range(2, n):
            fib = f_1 + f_2
            f_2 = f_1
            f_1 = fib
        return fib

def recursive_fib(n):
    if n <= 2:
        return 1
    else:
        return recursive_fib(n - 1) + recursive_fib(n - 2)

# Global array

FibArray = [1, 1]

def dynamic_fib(n):
    if n <= 2:
        return 1
    else:
        if n > len(FibArray):
            FibArray.append(dynamic_fib(n - 1) + dynamic_fib(n - 2))
        return FibArray[n - 1]

def test(title, function, start, end, cut):
    print(title)
    start_time = datetime.now()
    for i in range(start, end + 1):
        print(str(function(i)).rjust(8), end = ' ')
        if i % cut == 0:
            print()
    print('Duration {}'.format(datetime.now() - start_time))
    print()

print("Fibonacci numbers in 3 ways")
print("---")
test('Iterative', iterative_fib, 1, 36, 6)
test('Recursive', recursive_fib, 1, 36, 6)
test('Dynamic', dynamic_fib, 1, 36, 6)
