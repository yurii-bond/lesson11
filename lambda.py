def multiply(x, y):
    return print(x * y)


multiply(2, 2)
multiply(3, 3)

(lambda x, y: print(x * y))(2, 2)

mult = lambda x, y: print(x * y)

mult(3, 3)

lamb_da = lambda x, y, func: func(x, y)

lamb_da(2, 3, multiply)

_lambda = lambda x, y: print(f'My full name is: {x} {y}')

_lambda('Yurii', 'Bondarenko')


format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"

print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))

axb = multiply

axb(5, 4)
