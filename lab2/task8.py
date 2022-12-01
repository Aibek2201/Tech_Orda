def add(bank,a):
    bank += a
    return bank

def minus(bank,a):
    bank -= a
    return bank

def conversion(money, first, second):
    match first, second:
        case 'USD', 'KZT':
            return money * 470
        case 'KZT', 'USD':
            return money / 470
        case _:
            return 'Error'