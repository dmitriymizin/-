def test(*params, **values):
    print(params, values)


test(1, 2, 3, car='Kia', car_servise='Bosch_service')


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(7))