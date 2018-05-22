"""""
Module to convert one number to another with different numeral system
@author: Fanzil

"""""


def convert(number, baseInit, baseFinal):
    number = str(number)
    baseInit = int(baseInit)
    baseFinal = int(baseFinal)
    if baseInit < 2 or baseInit > 36 or baseFinal < 2 or baseFinal > 36:
        raise ValueError('Base of the number must be at least 2 and not more than 36!')
    if baseInit == 10:
        return convertDecimalToOther(number, baseFinal)
    if baseFinal == 10:
        return convertOtherToDecimal(number, baseInit)
    return convertDecimalToOther(convertOtherToDecimal(number, baseInit), baseFinal)


def convertOtherToDecimal(number, base):
    return int(number, base=base)


def convertDecimalToOther(number, base):
    if base == 2:
        return bin(number)[2:].upper()
    if base == 8:
        return oct(number)[2:].upper()
    if base == 16:
        return hex(number)[2:].upper()
    res = ''
    while number != 0:
        mod = number % base
        if base > 10:
            t = mod + 48
            if mod > 9:
                t += 7
            res += chr(t)
        else:
            res += str(mod)
        number //= base
    return res[::-1].upper()