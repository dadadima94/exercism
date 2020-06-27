# 13 passed in 7.78s


def classify(number):
    if number <= 0:
        raise ValueError('number negative or zero')

    aliquot = 0
    for i in range(1, number):
        if number % i == 0:
            aliquot += i

    if number == aliquot:
        return "perfect"
    elif aliquot > number:
        return "abundant"
    else:
        return "deficient"
