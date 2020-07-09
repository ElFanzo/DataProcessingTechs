"""Module for converting numbers to various numeral systems."""


def convert(number, base_init, base_final):
    """Convert a number to another numeral system.

    :param number: the initial number
    :param base_init: a base of the initial number
    :param base_final: a base of the final number
    :return: converted number
    """
    base_init = int(base_init)
    base_final = int(base_final)

    if not (1 < base_init < 37) or not (1 < base_final < 37):
        raise ValueError(
            "Base of the number must be at least 2 and not more than 36!"
        )

    if base_init == 10:
        return str(__convert_dec_to_other(number, base_final))
    if base_final == 10:
        return str(__convert_to_dec(number, base_init))
    return str(
        __convert_dec_to_other(
            __convert_to_dec(number, base_init), base_final
        )
    )


def __convert_to_dec(number, base):
    """Convert a number to the decimal numeral system.

    :param number: the initial number
    :param base: a base of the initial number
    :return: converted number
    """
    return int(str(number), base=base)


def __convert_dec_to_other(number, base):
    """Convert the decimal number to another numeral system.

    :param number: the initial number
    :param base: a base of the final number
    :return: converted number
    """
    number = int(number)

    if base == 2:
        return bin(number)[2:].upper()
    if base == 8:
        return oct(number)[2:].upper()
    if base == 16:
        return hex(number)[2:].upper()

    res = ""
    while number:
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
